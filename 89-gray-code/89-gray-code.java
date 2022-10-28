class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer> result = new ArrayList<>();
        result.add(0);
        int addition = 1;
        for (int i = 0; i < n; i++){
            int start = result.size() - 1;
            for (int j = start; j >= 0; j--){
                result.add(result.get(j) + addition);
            }
            addition *= 2;
        }
        return result;
    }
}
