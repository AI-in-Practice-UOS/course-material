from torch import nn


class ConvModel(nn.Module):

    def __init__(
        self, image_channels: int, depth: int, num_classes: int, channel_factor: int = 3
    ) -> None:
        super().__init__()
        in_channels = 8
        expand = nn.Conv2d(image_channels, in_channels, kernel_size=3, padding=1)

        blocks = []
        for i in range(depth):
            channels = in_channels * channel_factor**i
            out_channels = in_channels * channel_factor ** (i + 1)
            blocks.append(
                nn.Sequential(
                    SkipConv(channels=channels, kernel_size=3),
                    nn.Conv2d(
                        in_channels=channels,
                        out_channels=out_channels,
                        padding=1,
                        kernel_size=3,
                    ),
                    nn.MaxPool2d(kernel_size=3, stride=2),
                )
            )

        self.backbone = nn.Sequential(expand, *blocks)

        self.head = nn.Sequential(
            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten(),
            nn.Linear(in_channels * channel_factor**depth, num_classes),
        )

    def forward(self, input):
        x = self.backbone(input)
        return self.head(x)


class SkipConv(nn.Module):

    def __init__(self, channels, kernel_size):
        super().__init__()
        self.conv_1 = nn.Conv2d(channels, channels, kernel_size, padding=1)
        self.bn_1 = nn.BatchNorm2d(channels)
        self.conv_2 = nn.Conv2d(channels, channels, kernel_size, padding=1)
        self.bn_2 = nn.BatchNorm2d(channels, channels)

    def forward(self, input):
        x = self.conv_1(input)
        x = self.bn_1(x)
        x = self.conv_2(x)
        x = self.bn_2(x)
        return x + input
