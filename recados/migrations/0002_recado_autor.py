from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("recados", "0001_initial"),
    ]

    operations = [
        # Remove os recados antigos (que nao tinham autor) e o campo 'nome'.
        # Depois adiciona o vinculo obrigatorio com o usuario que publicou.
        migrations.RunSQL(
            sql="DELETE FROM recados_recado;",
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.RemoveField(
            model_name="recado",
            name="nome",
        ),
        migrations.AddField(
            model_name="recado",
            name="autor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recados",
                to=settings.AUTH_USER_MODEL,
                default=1,
            ),
            preserve_default=False,
        ),
    ]
