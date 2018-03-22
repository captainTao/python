<!-- 
待签名数据集 
待签名数据集是一个键值对集合
按照键名排好序再进行md5运算加密码


http://outofmemory.cn/code-snippet/939/python-liangzhong-produce-md5-method
python中实现md5的方法：
一. 使用md5包

import md5

src = 'this is a md5 test.'   
m1 = md5.new()   
m1.update(src)   
print m1.hexdigest()   
二. 使用hashlib

import hashlib   

m2 = hashlib.md5()   
m2.update(src)   
print m2.hexdigest()   
推荐使用第二种方法。

https://www.cnblogs.com/weiman3389/p/6056305.html
使用python求字符串或文件的MD5 五月 21st, 2008

#以下可在python3000运行。

#字符串md5,用你的字符串代替’字符串’中的内容。

import hashlib

md5=hashlib.md5(‘字符串’.encode(‘utf-8′)).hexdigest()

print(md5)

#求文件md5

import hashlib

#文件位置中的路径，请用双反斜杠，

如’D:\\abc\\www\\b.msi’ file='[文件位置]’

md5file=open(file,’rb’)

md5=hashlib.md5(md5file.read()).hexdigest()

md5file.close()

print(md5)
-->


<?php
require_once dirname(__FILE__).DIRECTORY_SEPARATOR.'..'.DIRECTORY_SEPARATOR.'vendors'
    .DIRECTORY_SEPARATOR.'Crypt3Des.php';
class SecurityHelper
{
    public static function sign($params, $secret)
    {
        if (is_array($params)) {
            $a = $params;
            $params = array();
            foreach ($a as $key => $value) {
                $params[] = "$key=$value";
            }
            sort($params);
            $params = implode('', $params);
        } elseif (is_string($params)) {
        } else {
            return false;
        }
        return self::pinguoMD5($params, $secret);
    }
    
    /**
     * pinguoMD5('111111','PINGUOSOFT')==c6aedc5fc311e463d4f119941474545d
     */
    public static function pinguoMD5($original, $key = 'PINGUOSOFT') 
    {
        $key_len = strlen($key);
        $key_empty = empty($key);
        $md5 = md5($original);
        $len = strlen($md5);
        $len = $len/2;
        /*
         echo '$original='.$original."\n";
        echo '$key='.$key."\n";
        echo '$md5='.$md5."\n";
        echo '$len='.$len."\n";
        echo "ch1, ch2, ch, cc\n";
        */
        $outString = '';
        for ($i = 0; $i < $len; $i ++) {
            //md5异或byKeys
            if (! $key_empty) {
                $ch1 = hexdec($md5[$i*2].$md5[$i*2+1]);
                $ch2 = ord($key[$i % $key_len]);
                $ch = ($ch1 ^ $ch2);
                //$cc = dechex( $ch );
                //echo "$ch1, $ch2, $ch, $cc\n";
            } else {
                $ch = $md5 [$i];
            }
            $outString .= $ch<=0xF?('0'.dechex($ch)):dechex($ch);
        }
        return $outString;
    }