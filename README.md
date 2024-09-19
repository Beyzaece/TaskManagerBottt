# Task Manager Bot

Bu bot, küçük ekiplerde görev yönetimi için tasarlanmıştır. Görev ekleme, silme, görüntüleme ve tamamlama gibi işlevlere sahiptir.

## Kullanım

1. `!add_task <açıklama>` - Yeni bir görev ekler.
2. `!delete_task <görev_id>` - Belirtilen ID'ye sahip bir görevi siler.
3. `!show_tasks` - Tüm görevleri listeler.
4. `!complete_task <görev_id>` - Belirtilen ID'ye sahip bir görevi tamamlanmış olarak işaretler.

## Gereksinimler

Projenizi çalıştırmak için gerekli bağımlılıklar:

- `discord.py`
- `sqlite3` (Python ile birlikte gelir)

### Kurulum

Gerekli kütüphaneleri yüklemek için terminalde aşağıdaki komutu çalıştırın:

```bash
pip install discord.py
