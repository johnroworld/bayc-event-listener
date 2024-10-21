from django.db import models

class TransferEvent(models.Model):
    token_id = models.BigIntegerField(db_index=True)
    from_address = models.CharField(max_length=42)
    to_address = models.CharField(max_length=42)
    transaction_hash = models.CharField(max_length=66)
    block_number = models.IntegerField()

    def __str__(self):
        return f"Transfer: {self.token_id} from {self.from_address}"