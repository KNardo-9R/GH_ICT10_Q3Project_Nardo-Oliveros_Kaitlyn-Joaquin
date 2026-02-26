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
        display(f'✅Step 1 is all good! You are registered for intrams.', target='outputsw2')
    else: 
        display(f'❌Please register online.', target='outputsw2')
    
    # medcert confirmation
    if med == 'confirmed':
        display(f'✅Step 2 is all good! You are physically fit to play.', target='outputsw2')
    else: 
        display(f'❌Please secure a medical clearance.', target='outputsw2')

    # Grade 7 Teams 
    if sec == '7-Ruby':
        display(f'Your section is Blue Bears.', target='outputsw2')
    elif sec == '7-Topaz': 
        display(f'Your section is Yellow Tigers.', target='outputsw2')
    elif sec == '7-Jade':
        display(f'Your section is Red Bulldogs.', target='outputsw2')
    elif sec == '7-Sapphire': 
        display(f'Your section is Green Hornets.', target='outputsw2')
    elif sec == '7-Emerald':  
        display(f'Your section is Red Bulldogs.', target='outputsw2')  
    elif sec == '8-Ruby':
        display(f'Your section is Yellow Tigers.', target='outputsw2')
    elif sec == '8-Topaz': 
        display(f'Your section is Blue Bears.', target='outputsw2')
    elif sec == '8-Sapphire': 
        display(f'Your section is Red Bulldogs.', target='outputsw2')
    elif sec == '8-Emerald':  
        display(f'Your section is Green Hornets.', target='outputsw2')  
    elif sec == '9-Ruby':
        display(f'Your section is Green Hornets.', target='outputsw2')
    elif sec == '9-Topaz': 
        display(f'Your section is Blue Bears.', target='outputsw2')
    elif sec == '9-Sapphire': 
        display(f'Your section is Red Bulldogs.', target='outputsw2')
    elif sec == '9-Emerald':  
        display(f'Your section is Yellow Tigers.', target='outputsw2')  
    elif sec == '10-Ruby':
        display(f'Your section is Blue Bears.', target='outputsw2')
    elif sec == '10-Topaz': 
        display(f'Your section is Red Bulldogs.', target='outputsw2')
    elif sec == '10-Sapphire': 
        display(f'Your section is Yellow Tigers.', target='outputsw2')
    elif sec == '10-Emerald':  
        display(f'Your section is Green Hornets.', target='outputsw2')  
    else: 
        display(f'❌Please recheck your section input.', target='outputsw2')


# ST PYTHON

# account creation

def signup(e): 
    document.getElementById('signresult').innerHTML = ' '

    # CONVERTING THE INPUTS 
    username = document.getElementById('user').value.lower() 
    password = document.getElementById('pass').value 

    # CHECKING THE INPUTS 
    # for username 
    username_characters = len(username) # checking # of characters in the username input

    # for password 
    password_characters = len(password) # checking # of characters in the password input 
    password_letters = any(passw.isalpha() for passw in password) # checking if input contains at least one letter 
    password_numbers = any(passw.isdigit() for passw in password) # checking if input contains at least one number 
    
    # For keyword = container for the iterable objects in the list =
    # In keyword to direct where to get the contents of the passw container, which is the password variable 


    # CHECKING IF INPUTS ARE APPLICABLE 
    # for username 
    if username_characters < 7: 
        display(f'❌Username needs at least 7 characters', target='signresult')
    else: 
        display(f'✅Username has 7 characters or more', target='signresult')

    # for password 
    if password_letters: 
        display (f'✅Password contains at least one letter', target='signresult')
    else: 
        display(f'❌Password needs to contain at least one letter', target='signresult')

    if password_numbers: 
        display (f'✅Password contains at least one number', target='signresult')
    else: 
        display(f'❌Password needs to contain at least one number', target='signresult')

    if password_characters < 10: 
        display(f'❌Password needs at least 10 characters',target='signresult')
    else: 
        display(f'✅Password has 10 or more characters', target='signresult')

# LIST OF PLAYERS PYTHON
    
        
