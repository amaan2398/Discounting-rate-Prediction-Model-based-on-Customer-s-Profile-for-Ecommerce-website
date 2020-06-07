<?php
class loyaltydiscount{
  public array $prodDiscount;
  public float $t;
  public $tax_toggle;
  public function __construct(array $prodDiscount, int $t)
  {
    $this->prodDiscount = $prodDiscount;
    $this->t = $t;

  }

}
 ?>
