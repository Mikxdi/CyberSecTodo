## Instructions
If you have done course part 2 exercises there will be nothing major to worry about.
Run python3 manage.py migrate
Run python3 manage.py shell < createdefault.py
Run python3 manage.py runserver
Server has now same default users as exercises had, alice:redqueen & bob:squarepants

### Flaw 1: SQL injection
The first security flaw in software is SQL injection, which can happen when data made by the attacker is sent to the server, where it might affect raw SQL database queries.

In the Todo app, vulnerability for SQL injection can be found in the delete function of the app. The app takes user input and adds it to the raw query without any safety checks. After this, the app should delete all Todos, where this input string is included in Todo.name. This causes the possibility for the attacker to add his own query to that raw query and for example delete all Todos in the database. 

Avoiding this problem is without a doubt very easy. In Django, there is already a model system, which takes care of risk injection attacks. This is done by escaping the query if it contains character strings that are seen as a possible security threat. These models are used in every else SQL query in-app. In this app, the fix would be changing the raw query to Todo.objects.filter(name_contains=’String’).

### Flaw 2: Broken access control
Broken access control means that authentication doesn’t correctly limit what the user is allowed to do inside the software. 
In application, there is broken access control done by using the GET method instead of POST. This is seen when you mark Todo as done. Because it’s done by the GET method and without making sure that the correct user is marking Todo, everyone can access Todos by making a request to server URL like “/mark_done?todo_name=something”. Also, the app doesn’t check if Todo is made by the user who is asking for done marking.

These could be easily avoided with two simple steps. First one would be using the POST method. Another fix that would be important to make, is making sure that the user is actually the one owning the Todo. This can be done by using “user = request.user” in the query to make sure it won’t do anything if a user isn’t the owner of Todo.

### Flaw 3: XSS risk
The risk for Cross-Site Scripting arises in the apps index.html template. XSS means that fields, where the user gives input, can be used to render something to the site or to run HTML scripts on the site. With this user can do malicious requests on the server with scripts if data isn’t filtered. The template has multiple fields, that are marked as safe when they bring the text from the server. This means Django won’t use it automated escape functions when it notices possible threat in the inputs made by the user. 

This is easily fixed by removing the safe tag from fields. It has literally no downsides in the software and the tags are only a threat to the app.

### Flaw 4:Broken authetication
Broken authentication means that there are flaws in app regarding authentication, that allow attack to have access to either passwords or session tokens, that allow attackers to get through to one’s session.
Broken authentication in this app is done by using session ID’s that are really easy to brute force with really simple for-loop based code. This is because the session ID follows the pattern, where the session ID is always “session-n” and “n” is always just incremented by 1. Just iterating through possible numbers until hitting correct one would be enough. 

The easiest fix to this would be using Djangos’s own SessionMiddleware. This middleware would generate way more safe and actually random session ID’s, which would make brute-forcing through them almost impossible.

### Flaw 5: Sensitive data exposure

Sensitive data exposure means that users’ data are easily accessible by attackers, because of poor encrypting, insecure transfer methods, or even just plain mistakes in storage. In the Todo app, there are two major contenders in this category. The first one is that every single user sees every Todo made. Even though Todo has information on its owner it doesn’t take it into account when listing all Todos. Another one is how add_todo works through the GET method. This means that even after the user has done the request if an attacker somehow has access to user’s browser or computer at all, an attacker can look up the request which is in form of /add_todo?todo_name=something&todo_desription=something. This contains literally all the information that is stored on a server in plaintext form.

Both of these are easily fixable. In the first problem, the fix would be adding a user check-in query. This could be done by adding user = request.user to query. For another point, the fix would chancing method to POST from GET. 
