class Solution:
    def minOperations(self, s):
        binary_num = len(s) * '0'
        len_binary_num = len(binary_num)
        target_s_list_1 = list(binary_num)
        len_target_s_list_1 = len(target_s_list_1)
        i = 0
        while (i < len_target_s_list_1):
            target_s_list_1[i] = '1'
            i += 2
        target_s_list_2 = list(binary_num)
        len_target_s_list_2 = len(target_s_list_2)
        i = 1
        while (i < len_target_s_list_2):
            target_s_list_2[i] = '1'
            i += 2
        count_ops_1 = 0
        i = 0
        while (i < len_target_s_list_1):
            if (target_s_list_1[i] != s[i]):
                count_ops_1 += 1
            i += 1
        count_ops_2 = 0
        i = 0
        while (i < len_target_s_list_2):
            if (target_s_list_2[i] != s[i]):
                count_ops_2 += 1
            i += 1
        return min(count_ops_1, count_ops_2)