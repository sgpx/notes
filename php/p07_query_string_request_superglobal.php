<?php

if($_SERVER["REQUEST_METHOD"] == "GET"){
    print_r($_REQUEST["queryparam1"]);
    print_r($_REQUEST["queryparam2"]);
}
