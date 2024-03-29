from config import app
from controller_functions import logout, index, login_page, login_check, register, dev_landing, dev_add_lang, dev_remove_lang, pos_add_lang, pos_remove_lang, dev_dash, create_dev_bio, org_landing, org_add_pos, new_position, edit_position, val_edit_pos,del_position, position_details, apply, unapply, email_check

app.add_url_rule("/logout", view_func=logout)
app.add_url_rule("/", view_func=index)
app.add_url_rule("/login_page", view_func=login_page)
app.add_url_rule("/login_check", view_func=login_check, methods=["POST"])
app.add_url_rule("/register", view_func=register, methods=["POST"])
app.add_url_rule("/dev_landing", view_func=dev_landing)
app.add_url_rule("/dev_add_lang/<lang_id>", view_func=dev_add_lang)
app.add_url_rule("/dev_remove_lang/<lang_id>", view_func=dev_remove_lang)
app.add_url_rule("/pos_add_lang/<lang_id>", view_func=pos_add_lang)
app.add_url_rule("/pos_remove_lang/<lang_id>", view_func=pos_remove_lang)
app.add_url_rule("/dev_dash", view_func=dev_dash)
app.add_url_rule("/create_dev_bio", view_func=create_dev_bio, methods=["POST"])
app.add_url_rule("/org_landing", view_func=org_landing)
app.add_url_rule("/org_add_pos", view_func=org_add_pos)
app.add_url_rule("/new_position", view_func=new_position, methods=["POST"])
app.add_url_rule("/edit_position/<pos_id>", view_func=edit_position)
app.add_url_rule("/val_edit_pos/<pos_id>", view_func=val_edit_pos, methods=["POST"])
app.add_url_rule("/del_position/<pos_id>", view_func=del_position)
app.add_url_rule("/position_details/<pos_id>", view_func=position_details)
app.add_url_rule("/apply/<pos_id>", view_func=apply)
app.add_url_rule("/unapply/<pos_id>", view_func=unapply)
app.add_url_rule("/email_check", view_func=email_check, methods=["POST"])