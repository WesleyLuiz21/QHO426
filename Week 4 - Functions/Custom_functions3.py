
def escape_by(plan):
    if plan == 'jumping over':
        print('We cannot escape that way! The boulder is too big!')
    elif plan == 'running around':
        print('We cannot escape that way! The boulder is moving too fast!')
    elif plan == 'cross bridge ahead':
        print('that might just work! lets go!')
    else:
        print('We cannot escape that way! The boulder is in the way!')

escape_by('jumping over')
escape_by('running around')
escape_by('cross bridge ahead')
