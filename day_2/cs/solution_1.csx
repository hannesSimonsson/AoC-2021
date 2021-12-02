string[] lines = System.IO.File.ReadAllLines(@"../input_1.txt");
List<(string, int)> input = lines.Select(line =>
                                                 {
                                                     var instruction = line.Split(' ');
                                                     return (instruction[0], int.Parse(instruction[1]));
                                                 }).ToList();

int depth = 0;
int horizontal = 0;

foreach ((string, int) line in input)
{
    string command = line.Item1;
    int value = line.Item2;

    switch (command)
    {
        case "forward":
            horizontal += value;
            break;
        case "down":
            depth += value;
            break;
        case "up":
            depth -= value;
            break;
    }
}

Console.Write(depth * horizontal);