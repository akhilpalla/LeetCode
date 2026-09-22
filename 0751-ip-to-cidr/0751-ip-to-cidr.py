class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        if n ==0:
            return []
        result = []
        ip_int = self.iptoInt(ip)
        tzb:int = self.countTrailingZerobits(ip_int)
        current_range = 2 ** tzb
        if current_range <= n:
            result.append(f'{ip}/{32-tzb}')
            return result + self.ipToCIDR(self.intToIp(ip_int + current_range), n - current_range)
        elif current_range > n:
            tzb = int(math.log(n, 2))
            result.append(f'{ip}/{32-tzb}')
            current_range = 2** tzb
            return result + self.ipToCIDR(self.intToIp(ip_int + current_range), n - current_range)
    def intToIp(self, number: int)-> str:
        a, b, c ,d =   number >>24 & 255, number >>16 & 255, number >>8 & 255, number & 255
        return f'{a}.{b}.{c}.{d}'
    def iptoInt(self, ip:str)-> int:
        splits = ip.split('.')
        a, b, c, d = int(splits[0]),int(splits[1]),int(splits[2]),int(splits[3])
        return (a<<24) + (b << 16) + (c << 8) + d
    def countTrailingZerobits(self, number:int)-> int:
        result = 0
        for i in range(0,32):
            if (number >> i) % 2 == 0:
                result = i+1
            else:
                return result
        return result