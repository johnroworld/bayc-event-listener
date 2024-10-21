import logging
from django.core.management.base import BaseCommand
from listener.services.blockchain import connect_to_blockchain, get_bayc_contract
from listener.models import TransferEvent
from web3.exceptions import PersistentConnectionError
from django.db import IntegrityError, DatabaseError, transaction

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            web3 = connect_to_blockchain()
        except PersistentConnectionError as e:
            self.stderr.write(f"Network error: {e}")
            logger.error(f"Failed to connect: {e}")
        except Exception as e:
            self.exception(f"An undexpected error occured: {e}")

        bayc_contract = get_bayc_contract(web3)

        # Fetch events from a recent block range
        START_BLOCK = web3.eth.block_number - 1000 # Adjust this range as needed
        END_BLOCK = 'latest'

        transfer_events = bayc_contract.events.Transfer.create_filter(
            from_block=START_BLOCK,
            to_block=END_BLOCK
        ).get_all_entries()

        for event in transfer_events:
            try:
                with transaction.atomic():
                    TransferEvent.objects.create(
                        token_id=event['args']['tokenId'],
                        from_address=event['args']['from'],
                        to_address=event['args']['to'],
                        transaction_hash=event['transactionHash'].hex(),
                        block_number=event['blockNumber']
                    )
                    self.stdout.write(f"Successfully saved transfer event for token {event.args.tokenId}")
            except IntegrityError as e:
                self.stderr.write(f"Database integrity error: {e}")
                logger.error(f"Failed to save transfer event: {e}")
            except DatabaseError as e:
                self.stderr.write(f"Database error: {e}")
                logger.error(f"Database issue during event save: {e}")
            except Exception as e:
                self.stderr.writable(f"Unexcepted error saving event: {e}")
                logger.exception(f"Unexpected error during event save: {e}")