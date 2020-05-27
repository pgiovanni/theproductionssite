<?php
    $userName = htmlspecialchars($_POST ['userName']);
    $userEmail = htmlspecialchars($_POST ['userEmail']);

    echo $userName, '', $userEmail;

?>