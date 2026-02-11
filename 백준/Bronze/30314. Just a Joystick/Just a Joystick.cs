namespace Solution {
  class Program {
    static void Main(string[] args) {

      int n = int.Parse(Console.ReadLine()!);

      string currentInitials = Console.ReadLine()!;
      string targetInitials = Console.ReadLine()!;

      int totalMoves = Enumerable.Range(0, n).Sum(i => {
        int currentChar = currentInitials[i];
        int targetChar = targetInitials[i];
        int distance = Math.Abs(currentChar - targetChar);
        return Math.Min(distance, 26 - distance);
      });

      Console.WriteLine(totalMoves);

    }
  }
}
