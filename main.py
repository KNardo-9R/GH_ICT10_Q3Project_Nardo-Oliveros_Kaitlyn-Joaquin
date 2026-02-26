from pyscript import display, document

# SW2 PYTHON
def checker(e): 
    document.getElementById('outputsw2').innerHTML = ' '

# getting and converting
    intrams = document.getElementById('cintrams').value.lower()
    med = document.getElementById('cmed').value.lower()
    sec = document.getElementById('levelsec').value

    # intrams confirmation
    if intrams == 'confirmed': 
        display(f'✅Step 1 is all good! You are registered for intrams.', target='output')
    else: 
        display(f'❌Please register online.', target='output')
    
    # medcert confirmation
    if med == 'confirmed':
        display(f'✅Step 2 is all good! You are physically fit to play.', target='output')
    else: 
        display(f'❌Please secure a medical clearance.', target='output')

    # Grade 7 Teams 
    if sec == '7-Ruby':
        display(f'Your section is Blue Bears.', target='output')
    elif sec == '7-Topaz': 
        display(f'Your section is Yellow Tigers.', target='output')
    elif sec == '7-Jade':
        display(f'Your section is Red Bulldogs.', target='output')
    elif sec == '7-Sapphire': 
        display(f'Your section is Green Hornets.', target='output')
    elif sec == '7-Emerald':  
        display(f'Your section is Red Bulldogs.', target='output')  
    elif sec == '8-Ruby':
        display(f'Your section is Yellow Tigers.', target='output')
    elif sec == '8-Topaz': 
        display(f'Your section is Blue Bears.', target='output')
    elif sec == '8-Sapphire': 
        display(f'Your section is Red Bulldogs.', target='output')
    elif sec == '8-Emerald':  
        display(f'Your section is Green Hornets.', target='output')  
    elif sec == '9-Ruby':
        display(f'Your section is Green Hornets.', target='output')
    elif sec == '9-Topaz': 
        display(f'Your section is Blue Bears.', target='output')
    elif sec == '9-Sapphire': 
        display(f'Your section is Red Bulldogs.', target='output')
    elif sec == '9-Emerald':  
        display(f'Your section is Yellow Tigers.', target='output')  
    elif sec == '10-Ruby':
        display(f'Your section is Blue Bears.', target='output')
    elif sec == '10-Topaz': 
        display(f'Your section is Red Bulldogs.', target='output')
    elif sec == '10-Sapphire': 
        display(f'Your section is Yellow Tigers.', target='output')
    elif sec == '10-Emerald':  
        display(f'Your section is Green Hornets.', target='output')  
    else: 
        display(f'❌Please recheck your section input.', target='output')


# ST PYTHON

