https://leetcode.com/problems/decompress-run-length-encoded-list/

``` php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function decompressRLElist($nums) {
        $return = array();
        for( $i =0; $i< count($nums); $i+=2 ){
                for( $j=0; $j < $nums[$i]; $j++){
                        $return[] = $nums[$i+1];
                }
        }
        return $return; 
    }
}
```