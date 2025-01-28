namespace Solution {
  class Program {
    static void Main(string[] args) {

      var n = int.Parse(Console.ReadLine()!);

      for (var i = 0; i < n; i++) {
        var input = Console.ReadLine()?.Split(' ');
        var a1 = int.Parse(input![0]);
        var p1 = int.Parse(input![1]);
        input = Console.ReadLine()?.Split(' ');
        var r1 = int.Parse(input![0]);
        var p2 = int.Parse(input![1]);

        double sliced = (double)a1 / p1;
        double whole = (double)(Math.PI * Math.Pow(r1, 2)) / p2;

        if (sliced > whole) Console.WriteLine("Slice of pizza");
        else Console.WriteLine("Whole pizza");
      }

    }
  }
}