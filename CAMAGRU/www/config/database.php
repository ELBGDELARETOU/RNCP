<?php
$DB_DSN = 'mysql:host=mysql;dbname=camagru;charset=utf8';
$DB_USER = 'root';
$DB_PASSWORD = 'root';

try {
    $pdo = new PDO($DB_DSN, $DB_USER, $DB_PASSWORD);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Erreur de connexion : " . $e->getMessage());
}