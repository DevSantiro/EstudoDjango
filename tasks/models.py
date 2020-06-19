from django.db import models

class Task(models.Model):

    STATUS = (
        ('doing','Doing'),
        ('done','Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Sequencia(models.Model):

    TIPO = (
        ('dna','DNA'),
        ('rna','RNA'),
        ('proteina', 'PROTEINA')
    )    

    cabecalho = models.CharField(max_length=255)
    sequencia = models.TextField()
    tipo      = models.CharField(
        max_length=8,
        choices=TIPO,
    )

class mSequencia(models.Model):

    TIPO = (
        ('dna','DNA'),
        ('rna','RNA'),
        ('proteina', 'PROTEINA')
    ) 

    titulo = models.CharField(max_length=255)
    fasta = models.FileField(upload_to='sequencias/fasta/')
    tipo      = models.CharField(
        max_length=8,
        choices=TIPO,
    )

    def __str__(self):
        return self.titulo

class Proteina(models.Model):
    titulo = models.CharField(max_length=255)
    sequencia = models.TextField()
    
    def __str__(self):
        return self.titulo