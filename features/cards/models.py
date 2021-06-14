from django.db import models


class Card(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    front_text = models.CharField(max_length=20, help_text="Front text")
    back_text = models.CharField(max_length=20, help_text="Back text")
    created_at = models.TimeField(auto_created=True)
    updated_at = models.TimeField(auto_now=True)

    def update_card(self, front_text=front_text, back_text=back_text):
        self.front_text = front_text if front_text else self.front_text
        self.back_text = back_text if back_text else self.back_text
        self.save()

    @classmethod
    def get_card_by_id(cls, id):
        return cls.objects.get(pk=id)

    @classmethod
    def get_all_cards(cls):
        return cls.objects.get()

    def save_card(self):
        self.save()

    def delete_card(self):
        self.delete()

    class Meta:
        db_table = 'cards'
