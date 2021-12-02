string[] lines = System.IO.File.ReadAllLines(@"../input_1.txt");
int[] input = lines.Select(int.Parse).ToArray();


int window = 3;
int depth = 0;
int preDepth = input.Take(window).Sum(); // couldn't use input[..window] or input.Range(0, window)?
int acc = 0;

for (int i = 0; i < input.Length; i++)
{
    depth = input.Skip(i).Take(window).Sum();

    if (depth > preDepth)
        acc++;

    preDepth = depth;
}

Console.WriteLine(acc);