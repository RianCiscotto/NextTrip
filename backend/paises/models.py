from django.db import models

class Pais(models.Model):
    STATUS_CHOICES = [
        {'VISITEI','Visitei'},
        {'PRETENDO IR','Pretendo Ir'},
        {'NAO PRETENDO IR','Não Pretendo Ir'},
        {'NAO ADICIONADO','Não Adicionado'},
        
    ]
    
    
    
    nome = models.CharField(max_length=100, blank=True, null=True)
    populacao = models.IntegerField(blank=True, null=True)
    curiosidade = models.CharField(max_length=10000, blank=True, null=True)  
    bandeira = models.ImageField(upload_to='bandeiras/', blank=True, null=True)
    
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, blank=True, null=True, default='Não Adicionado')
    def __str__(self):
        return self.nome