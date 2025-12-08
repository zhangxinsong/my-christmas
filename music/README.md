# 🎵 音乐文件夹说明

## 使用方法

将您的圣诞音乐文件放入此文件夹，并命名为以下之一：

- `christmas.mp3` （推荐）
- `christmas.ogg` （备选格式）

## 支持的音频格式

- **MP3** - 最广泛支持，推荐使用
- **OGG** - 开源格式，作为备选
- **WAV** - 高质量但文件较大

## 音频文件要求

- **推荐时长**: 2-5分钟（会自动循环播放）
- **推荐码率**: 128-320 kbps
- **文件大小**: 建议小于10MB以优化加载速度

## 获取圣诞音乐

您可以从以下来源获取免费的圣诞音乐：

1. **YouTube Audio Library** - https://www.youtube.com/audiolibrary
2. **Free Music Archive** - https://freemusicarchive.org
3. **Incompetech** - https://incompetech.com
4. **Bensound** - https://www.bensound.com

⚠️ **注意**: 请确保使用的音乐是免费或您拥有使用权的，以避免版权问题。

## 配置选项

您可以在 `config.json` 中自定义音频设置：

```json
"audio": {
  "enabled": true,           // 是否启用音乐
  "autoplay": true,          // 是否自动播放
  "defaultVolume": 0.5,      // 默认音量 (0.0-1.0)
  "fadeIn": true,            // 是否启用淡入效果
  "fadeInDuration": 2000,    // 淡入时长(毫秒)
  "sources": [
    "./music/christmas.mp3",
    "./music/christmas.ogg"
  ]
}
```

## 控制说明

### 鼠标控制
- **右下角音乐控制面板**:
  - 播放/暂停按钮
  - 静音/取消静音按钮
  - 音量滑块 (0-100%)

### 键盘快捷键
- `M` - 播放/暂停音乐
- `N` - 静音/取消静音
- `H` - 隐藏所有UI（包括音乐控制）

## 自动播放说明

由于浏览器的自动播放策略，音乐可能无法在页面加载时自动播放。如果发生这种情况：

1. 页面会显示一个友好的提示界面
2. 点击"开始播放"按钮即可启动音乐
3. 音乐会以淡入效果开始播放

## 性能优化

- 当浏览器标签页失焦时，音乐会自动暂停以节省资源
- 重新聚焦时，音乐会自动恢复播放
- 音量设置会保存在浏览器本地存储中

## 故障排除

### 音乐无法播放
1. 检查音频文件是否存在于 `music` 文件夹
2. 确认文件名为 `christmas.mp3` 或 `christmas.ogg`
3. 检查浏览器控制台是否有错误信息
4. 尝试使用不同的浏览器

### 音乐加载缓慢
1. 压缩音频文件以减小大小
2. 使用更低的码率（如128kbps）
3. 将音频文件托管到CDN

### 自动播放被阻止
- 这是正常的浏览器行为
- 点击页面上的"开始播放"按钮即可
- 某些浏览器需要用户交互后才能播放音频

## 示例音频文件

如果您没有合适的圣诞音乐，可以搜索以下关键词：

- "Jingle Bells instrumental"
- "Silent Night piano"
- "Christmas ambient music"
- "Winter wonderland background music"

---

**注意**: 此文件夹当前为空，请添加您自己的音乐文件。
