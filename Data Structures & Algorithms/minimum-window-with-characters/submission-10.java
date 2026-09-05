class Solution {
    public String minWindow(String s, String t) {
        if (t.length() > s.length()) {
            return "";
        }

        int[] count = new int[128];

        // Đếm số lần xuất hiện của từng ký tự trong t
        for (char c : t.toCharArray()) {
            count[c]++;
        }

        int left = 0;
        int right = 0;

        int need = t.length();
        int minLength = Integer.MAX_VALUE;
        int minLeft = 0;

        while (right < s.length()) {

            char c = s.charAt(right);

            // Nếu c là ký tự mà t cần
            if (count[c] > 0) {
                need--;
            }

            count[c]--;
            right++;

            // Window hiện tại đã chứa đủ t
            while (need == 0) {

                // Cập nhật đáp án
                if (right - left < minLength) {
                    minLength = right - left;
                    minLeft = left;
                }

                char leftChar = s.charAt(left);

                count[leftChar]++;

                // Sau khi bỏ leftChar, window không còn đủ t
                if (count[leftChar] > 0) {
                    need++;
                }

                left++;
            }
        }

        return minLength == Integer.MAX_VALUE
                ? ""
                : s.substring(minLeft, minLeft + minLength);
    }
}