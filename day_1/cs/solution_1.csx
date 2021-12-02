string[] lines = System.IO.File.ReadAllLines(@"../input_1.txt");
int[] input = lines.Select(int.Parse).ToArray();

int preDepth = input[0];
int acc = 0;

foreach (int depth in input)
{
    if (depth > preDepth)
        acc++;

    preDepth = depth;
}

Console.WriteLine(acc);