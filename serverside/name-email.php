<?php
    $name = htmlspecialchars($_POST ['name']);
    $email = htmlspecialchars($_POST ['email']);

    echo $name, '', $email;

?>