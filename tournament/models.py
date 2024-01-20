from django.db import models

# Create your models here.
class Tournament(models.Model): 
    
    Tournament_Name = models.CharField(max_length=150)
    Game_Name = models.CharField(max_length=150)
    Tournament_Entry_Fees = models.IntegerField()
    Prize_Pool_in_Rupees = models.IntegerField()
    Registration_STARTS_ON = models.DateTimeField()
    Registration_ENDS_ON = models.DateTimeField()
    Tournament_STARTS_ON = models.DateTimeField()
    Tournament_ENDS_ON = models.DateTimeField()
    Tournament_Description = models.TextField(255)
    Streaming_On_channel_name = models.CharField(max_length=150)
    Tournament_Image = models.ImageField(upload_to='media/images')
    Game_Rules_and_Regulations = models.TextField(255)

    data_display = ("Tournament_Name", "Game_Name", "Tournament_Entry_Fees","Prize_Pool_in_Rupees","Registration_STARTS_ON","Registration_ENDS_ON","Tournament_STARTS_ON","Tournament_ENDS_ON","Tournament_Description","Streaming_On_channel_name","Tournament_Image","Game_Rules_and_Regulations")

    def __str__(self):
        return self.Tournament_Name
