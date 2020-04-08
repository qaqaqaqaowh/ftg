from textwrap import dedent

def templates_layout(name):
    return dedent(f"""\
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <link rel="shortcut icon" href="{{{{ url_for('static', filename='image/favicon.ico') }}}}">

        {{% assets "home_css" %}}
          <link rel="stylesheet" href="{{{{ ASSET_URL }}}}">
        {{% endassets %}}

        {{% assets "home_js" %}}
          <script type="text/javascript" src="{{{{ ASSET_URL }}}}"></script>
        {{% endassets %}}

        {{% block header %}}
        {{% endblock %}}

        <title>
          {{% block title %}}
          {{% endblock %}}{name}
        </title>

      </head>
      <body>
        {{% block content %}}
        {{% endblock %}}
        <footer>
          Made with &hearts; at <a target="_blank" href="https://www.nextacademy.com/?utm_source=github&utm_medium=student-challenge&utm_campaign=flask-nextagram">NEXT Academy</a>
        </footer>
      </body>
    </html>
    """)