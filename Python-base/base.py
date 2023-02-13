def index(request):
    number = {
        'fruits': ['apple','banana','grapes'],

    }
    return render(request,'index.html',number)


<h2>name is {{name}}</h2>
    <h2>age is {{age}}</h2>
    <h2>place is {{place}}</h2>

    {% if num1 > 0  %}

       <h2>positive number</h2>
    {% elif num1 < 0 %}
      
      <h2>negative number</h2>

    {% else %}
      <h2>number is zero</h2>

    {% endif %}<br>

    {% for n in fruits  %}
       <h2>{{n}}</h2>
    {% endfor %}
