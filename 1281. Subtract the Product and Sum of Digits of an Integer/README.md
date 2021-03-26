https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function subtractProductAndSum($n) {
        $array = str_split($n);
        $mul = 1; $add = 0;
        for( $i = 0; $i < count($array); $i++ ){
                $mul *= $array[$i];
                $add += $array[$i];
        }
        return $mul - $add;       
    }
}
```