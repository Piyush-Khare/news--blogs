
function login()
{
    var username = document.getElementById('loginEmail').value
    var password = document.getElementById('loginPassword').value
    var csrf = document.getElementById('csrf').value

    var data = {
        'username' : username,
        'password' : password
    }

    fetch('/api/login/' , {
        method : 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrf
        },
        
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        
        if(response.status == 200)
        {
            window.location.href = '/'
        }
        else
        {
            alert(response.message)
        }
    })
}




function signup()
{
    var email = document.getElementById('signupEmail').value
    var password = document.getElementById('signupPassword1').value
    var password1 = document.getElementById('signupPassword2').value
    var first_name = document.getElementById('signupName').value
    var csrf = document.getElementById('csrf').value

    var data = {
        'email' : email,
        'password' : password,
        'password1': password1,
        'first_name' : first_name
    }

    if (password != password1)
    {
        alert('Confirm Password not Matched')
    }
    else
    {
        fetch('/api/register/' , {
            method : 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken' : csrf,
            },
           
            body : JSON.stringify(data)
        }).then(result => result.json())
        .then(response => {
            console.log(response)
            if(response.status == 200){
                alert('User Registered, Please login yourself')
                window.location.href = '/login/'
            }
            else{
                alert(response.message)
            }
    
        })
    }
}