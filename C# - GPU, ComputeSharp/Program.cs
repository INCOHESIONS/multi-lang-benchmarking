#pragma warning disable CA1416

using ComputeSharp;
using System.Diagnostics;
using System.Globalization;
using System.IO;
using System.Linq;
using System;

const string CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

string RandomCharacters(int length = 10)
{
    var random = new Random();
    return string.Join("", (from _ in Enumerable.Range(0, length) select CHARS[random.Next(0, CHARS.Length)]).ToArray()) ?? "error";
}

var width = Convert.ToInt32(args[0]);
var height = Convert.ToInt32(args[1]);
var numberOfPoints = Convert.ToInt32(args[2]);
var saveImage = args[3] == "true";

var device = GraphicsDevice.GetDefault();
var random = new Random();

using var points = device.AllocateReadOnlyBuffer([.. Enumerable.Range(0, numberOfPoints).Select(_ => new float2(random.Next(0, width), random.Next(0, height)))]);
using var texture = device.AllocateReadWriteTexture2D<Rgba32, float4>(width, height);

var watch = new Stopwatch();
watch.Start();

device.ForEach(texture, new WorleyNoise(points));

watch.Stop();

Console.WriteLine((watch.ElapsedMilliseconds / 1000.0).ToString(CultureInfo.InvariantCulture));

if (!saveImage) return;

Directory.CreateDirectory("img/");
texture.Save($"img/{RandomCharacters()}.png");

[ThreadGroupSize(DefaultThreadGroupSizes.XY)]
[GeneratedComputeShaderDescriptor]
internal readonly partial struct WorleyNoise(ReadOnlyBuffer<float2> points) : IComputeShader<float4>
{
    public float4 Execute()
    {
        float minDist = float.MaxValue;

        for (int i = 0; i < points.Length; i++)
            minDist = Hlsl.Min(minDist, Hlsl.Dot(points[i] - ThreadIds.XY, points[i] - ThreadIds.XY));

        float color = 1.0F - Hlsl.Clamp(Hlsl.Sqrt(minDist), 0.0F, 255.0F) / 255.0F;

        return new float4(color, color, color, 1.0F);
    }
}
