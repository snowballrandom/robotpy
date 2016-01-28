<!DOCTYPE html>

<html>
<head>
    <title>Robot Controler</title>
<style>
  body{
      width:1024px;
      background:#efefef;
      }    
</style>
    
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
<script>        
    function action(val){

     var time = $('#cords').find('input[name="'+val+'"]').val();
     
     dataString = {
         action : val,
         time : time
     };
     
     $.ajax({
        type: "POST",
        url: 'robot.php',
        data: dataString,
        async:true,
        cache: true,
        success: function(html){
         console.log(html);
      }
     });
      return false;
      
    };
</script>
</head>

<body>

<div>
    <p>
        <form action="index.php" id="cords">
          <ul style="text-decoration: none;list-style: none;">
          <li><label>Forward Time</label></li>
          <li><input type="text" name="forward"/></li>
          <li><label>Reverse Time</label></li>
          <li><input type="text" name="backward"/></li>
          <li><label>Left Time</label></li>
          <li><input type="text" name="left"/></li>
          <li><label>Right Time</label></li>
          <li><input type="text" name="right" value="0"/></li>
          <li><label>Take Picture qty:</label></li>
          <li><input type="text" name="take" value="0"/></li>
        </form>
    </p>
</div>    
<?php include 'robot.php'; ?>

<button id="left" onclick="action('left')" value="Left">Left</button>
<button id="forward" onclick="action('forward')" value="Forward">Forward</button>
<button id="back" onclick="action('backward')" value="Backward">Backward</button>
<button id="right" onclick="action('right')" value="Right">Right</button>
<button id="pic" onclick="action('takepicture')" value="TakePic">Take Picture</button>



<ul style="background-color:#deefee;">
    
<?php

if ($handle = opendir('/srv/python/images/')) {
    while (false !== ($entry = readdir($handle))) {
        if ($entry != "." && $entry != "..") {
            echo '<li><a href="images/'.$entry.'">'.$entry.'</a></li>';
        }
    }
    closedir($handle);
}
?>
</ul>
</body>
</html>