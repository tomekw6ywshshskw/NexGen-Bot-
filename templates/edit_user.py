<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edytuj użytkownika: {{ user['user_id'] }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Edytuj użytkownika: {{ user['user_id'] }}</h1>
    <form method="POST">
        <label for="xp">XP:</label>
        <input type="number" name="xp" value="{{ user['xp'] }}">
        <label for="balance">Saldo:</label>
        <input type="number" name="balance" value="{{ user['balance'] }}">
        <button type="submit">Zapisz</button>
    </form>
    <a href="{{ url_for('user', id=user['id']) }}">Powrót do użytkownika</a>
</body>
</html>
