
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recados', '0002_recado_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='recado',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='recados/'),
        ),
    ]
