from django.http import HttpResponse
from djangoForEveryone.settings import UNIQUE_CODE

def index(reqeuest):
    return HttpResponse(f"Hello {UNIQUE_CODE}")

def index2(reqeuest):
    return HttpResponse('''
    <a>Answer to the Ultimate Question</a>
    <form>
        <input type="radio" id="html" name="choice" value="HTML">
        <label for="html">42</label><br>
        <input type="radio" id="css" name="choice" value="CSS">
        <label for="css">CSS</label><br>
        <input type="radio" id="javascript" name="choice" value="JavaScript">
        <label for="javascript">JavaScript</label> 
        <input type="text" id="username" name="username" value="JavaScript">
        <button>Vote</button>
        <button>Vote again?</button>
        <button>Log in</button>
    </form>
    ''')