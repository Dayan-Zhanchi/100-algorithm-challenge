class HanoiTower{

    public static void hanoi(int disk, String source, String dest, String spare){
        if(disk == 1){
            System.out.println("Move disk from " + source + " to " + dest);
        }
        else{
            hanoi(disk-1, source, spare, dest);
            hanoi(1, source, dest, spare);
            hanoi(disk-1, spare, dest, source);
        }
    }

    public static void main(String[] args){
        hanoi(3, "A", "B", "C");
    }
}