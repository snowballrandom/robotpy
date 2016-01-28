<?php
class robot{
    
    private $robot_on = FALSE;
    
    private $action      = null;
    private $time        = 0;
    private $multi       = FALSE;
    private $forward_mov = 0;
    private $reveres_mov = 0;
    private $left_mov    = 0;
    private $right_mov   = 0;
    
    private $take_pic     = FALSE;
    
    public function __construct(){
        $this->__init();  
    }
    
    private function __init(){
          
      $this->robot_on = TRUE;

        if(isset($_POST['action'])){
            if($_POST['action'] === 'takepicture'){
              $this->action = ($_POST['action']);
            }else{
              $this->action   = escapeshellarg($_POST['action']);   
            }
        } 
        if(isset($_POST['time'])){
          $this->time = escapeshellarg($_POST['time']);
        }                
                
        echo $this->main();
    }
    
    private function main(){
      echo $this->action();
    }
    
    private function action(){
            
        if(($this->action == 'takepicture')){
          return $this->take();
        }
        if(strcmp($this->action, 'forward')){
          return $this->forward();
        }
        if(strcmp($this->action, 'backward')){
          return $this->backward();
        }
        if(strcmp($this->action, 'right')){
          return $this->right();
        }
        if(strcmp($this->action, 'left')){
          return $this->left();
        }            
                             
    }
    
    private function forward(){
        
      $com = 'sudo python /srv/python/actions.py '.$this->action.' '.$this->time;
      $com = escapeshellcmd($com);
      $output='';
      $ret_code='';
      $ishell = exec($com, $output, $ret_code);
      return json_encode($ishell);
    }
    private function backward(){
        
      $com = 'sudo python /srv/python/actions.py '.$this->action.' '.$this->time;
      $com = escapeshellcmd($com);
      $output='';
      $ret_code='';
      $ishell = exec($com, $output, $ret_code);
      return true;
      
    }    
    private function right(){
        
      $com = 'sudo python /srv/python/actions.py '.$this->action.' '.$this->time;
      $com = escapeshellcmd($com);
      $output='';
      $ret_code='';
      $ishell = exec($com, $output, $ret_code);
      return true;
    } 
    private function left(){
        
      $com = 'sudo python /srv/python/actions.py '.$this->action.' '.$this->time;
      $com = escapeshellcmd($com);
      $output='';
      $ret_code='';
      $ishell = exec($com, $output, $ret_code);
      return true;
    }    
        
    public function take(){
        
     $image_name = 'image.jpg';
      $com = 'sudo fswebcam /srv/python/images/image'.time().'.jpg';
      $com = escapeshellcmd($com);
      $output='';
      $ret_code='';
      $ishell = shell_exec($com);
      return true;
    }

}

$robot = new robot;