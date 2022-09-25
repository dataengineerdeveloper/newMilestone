msg_template = """Hello {name},
thank you for joining {website}. we are very happu to have you
with us."""
#.format(name="Justin",websitrte='cfe.sh')

def format_msg(my_name='justin',my_website='cfe.sh'):
    my_msg=msg_template.format(name=my_name, website=my_website)
    return my_msg