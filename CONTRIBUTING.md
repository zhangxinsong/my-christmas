# 贡献指南

感谢你对本项目的关注！虽然这是一个个人学习项目，但我们欢迎任何形式的贡献和反馈。

---

## 📋 目录

- [行为准则](#-行为准则)
- [如何贡献](#-如何贡献)
- [报告 Bug](#-报告-bug)
- [提出功能请求](#-提出功能请求)
- [提交代码](#-提交代码)
- [代码规范](#-代码规范)
- [开发环境搭建](#-开发环境搭建)
- [测试指南](#-测试指南)

---

## 📜 行为准则

### 我们的承诺

为了营造一个开放和友好的环境，我们承诺：

- 尊重不同的观点和经验
- 接受建设性的批评
- 关注对社区最有利的事情
- 对其他社区成员表示同理心

### 不可接受的行为

- 使用性化的语言或图像
- 人身攻击或侮辱性评论
- 公开或私下的骚扰
- 未经许可发布他人的私人信息

---

## 🤝 如何贡献

### 贡献类型

你可以通过以下方式贡献：

1. **报告 Bug** - 发现问题并报告
2. **功能建议** - 提出新功能想法
3. **文档改进** - 改善文档质量
4. **代码贡献** - 修复 Bug 或实现新功能
5. **测试** - 在不同环境测试项目
6. **翻译** - 提供多语言支持

---

## 🐛 报告 Bug

### 在提交 Bug 之前

1. **检查已知问题** - 查看 [CHANGELOG.md](CHANGELOG.md) 的已知问题章节
2. **搜索现有 Issues** - 避免重复报告
3. **尝试最新版本** - 确保使用最新版本
4. **收集信息** - 准备详细的错误信息

### 如何提交 Bug 报告

使用 [Bug Report 模板](.github/ISSUE_TEMPLATE/bug_report.md) 创建 Issue，包含：

**必需信息**：
- **问题描述** - 清晰简洁的描述
- **复现步骤** - 详细的重现步骤
- **预期行为** - 你期望发生什么
- **实际行为** - 实际发生了什么
- **环境信息**：
  - 操作系统（Windows/macOS/Linux）
  - 浏览器及版本
  - 项目版本
  - 照片数量和格式

**可选信息**：
- 错误截图
- 浏览器控制台日志
- 配置文件内容
- 相关文件

**示例**：

```markdown
### 问题描述
图片加载时出现内存溢出错误

### 复现步骤
1. 放入 200 张 4K 分辨率照片到 images/ 文件夹
2. 启动本地服务器
3. 打开浏览器访问
4. 观察控制台错误

### 预期行为
图片应该正常加载并压缩

### 实际行为
浏览器崩溃，控制台显示 "Out of Memory"

### 环境
- 操作系统: Windows 11
- 浏览器: Chrome 120
- 项目版本: v3.0
- 照片数量: 200 张（每张 8MB）
```

---

## 💡 提出功能请求

### 在提交功能请求之前

1. **检查现有功能** - 确保功能尚未实现
2. **搜索现有请求** - 避免重复
3. **考虑适用性** - 功能是否适合项目定位

### 如何提交功能请求

使用 [Feature Request 模板](.github/ISSUE_TEMPLATE/feature_request.md) 创建 Issue，包含：

**必需信息**：
- **功能描述** - 清晰描述想要的功能
- **使用场景** - 为什么需要这个功能
- **解决方案** - 你希望如何实现
- **替代方案** - 是否有其他解决方法
- **优先级** - 低/中/高

**示例**：

```markdown
### 功能描述
支持从 URL 加载图片

### 使用场景
用户希望展示在线相册的照片，而不需要下载到本地

### 解决方案
添加配置选项 `loader.sources`，支持指定图片 URL 列表

### 替代方案
使用浏览器扩展下载图片后再加载

### 优先级
中等 - 对部分用户有用，但不影响核心功能
```

---

## 📤 提交代码

### Pull Request 流程

1. **Fork 项目** - 在 GitHub 上 Fork 本仓库
2. **克隆仓库** - Clone 你的 Fork 到本地
   ```bash
   git clone https://github.com/你的用户名/christmas-tree.git
   cd christmas-tree
   ```

3. **创建分支** - 基于 main 分支创建新分支
   ```bash
   git checkout -b feature/你的功能名
   # 或
   git checkout -b fix/bug描述
   ```

4. **开发功能** - 进行代码修改
   - 遵循代码规范
   - 添加必要的注释
   - 更新相关文档

5. **测试** - 确保所有功能正常
   - 在多个浏览器测试
   - 测试不同配置
   - 检查控制台无错误

6. **提交代码** - 提交你的更改
   ```bash
   git add .
   git commit -m "feat: 添加功能描述"
   ```

7. **推送分支** - 推送到你的 Fork
   ```bash
   git push origin feature/你的功能名
   ```

8. **创建 PR** - 在 GitHub 上创建 Pull Request
   - 使用 [PR 模板](.github/PULL_REQUEST_TEMPLATE.md)
   - 填写详细的描述
   - 关联相关 Issue

### PR 审核标准

你的 PR 需要满足：

✅ **代码质量**
- 代码遵循项目规范
- 逻辑清晰，易于理解
- 适当的错误处理

✅ **功能完整**
- 功能完全实现
- 边界情况处理
- 向后兼容

✅ **文档完善**
- 更新 README.md（如需要）
- 更新 CHANGELOG.md
- 添加代码注释

✅ **测试通过**
- 在 Chrome/Firefox/Edge 测试
- 不同配置下测试
- 无控制台错误

---

## 📝 代码规范

### JavaScript 代码规范

**命名规范**：
```javascript
// 变量和函数：驼峰命名
const myVariable = 10;
function myFunction() {}

// 常量：大写下划线
const MAX_IMAGES = 500;
const DEFAULT_VOLUME = 0.5;

// 类名：帕斯卡命名
class MyClass {}
```

**注释规范**：
```javascript
// 单行注释使用 //，注释前空一行

/**
 * 多行注释使用这种格式
 * @param {number} value - 参数描述
 * @returns {boolean} 返回值描述
 */
function example(value) {
    return value > 0;
}

// 关键代码段使用分隔符
// ==================== 模块名称 ====================
```

**代码风格**：
```javascript
// 使用 4 空格缩进
if (condition) {
    // 代码
}

// 大括号不换行
function example() {
    return true;
}

// 使用严格相等
if (value === 10) {}

// 优先使用 const，其次 let，避免 var
const a = 1;
let b = 2;
```

### HTML/CSS 规范

**HTML**：
```html
<!-- 使用语义化标签 -->
<main>
    <section>
        <h1>标题</h1>
    </section>
</main>

<!-- 属性使用双引号 -->
<div class="container" id="main">
```

**CSS**：
```css
/* 使用 kebab-case 命名 */
.my-class-name {
    /* 属性按字母顺序排列 */
    background-color: #000;
    color: #fff;
    margin: 10px;
}
```

### 配置文件规范

**JSON**：
```json
{
  "key": "value",
  "nested": {
    "key": "value"
  }
}
```
- 使用 2 空格缩进
- 键名使用驼峰命名
- 无尾随逗号

---

## 🛠️ 开发环境搭建

### 前置要求

- **浏览器**: Chrome 90+ / Firefox 88+ / Edge 90+
- **HTTP 服务器**: Python 3.6+ 或 Node.js
- **编辑器**: VS Code（推荐）
- **Python**: 3.6+（用于图片工具）

### 设置步骤

1. **克隆项目**
   ```bash
   git clone https://github.com/你的用户名/christmas-tree.git
   cd christmas-tree
   ```

2. **安装 Python 依赖**（可选）
   ```bash
   pip install Pillow
   ```

3. **启动开发服务器**
   ```bash
   python -m http.server 8000
   ```

4. **访问应用**
   ```
   http://localhost:8000/christmas.html
   ```

5. **安装推荐的 VS Code 扩展**
   - Live Server
   - ESLint
   - Prettier

### 开发工具配置

**VS Code 配置**（`.vscode/settings.json`）：
```json
{
  "editor.tabSize": 4,
  "editor.insertSpaces": true,
  "files.eol": "\n",
  "editor.formatOnSave": true
}
```

---

## 🧪 测试指南

### 手动测试清单

**基础功能**：
- [ ] 页面正常加载
- [ ] 图片成功加载
- [ ] 粒子系统运行流畅
- [ ] FPS 稳定在 55+

**手势控制**：
- [ ] 握拳切换到树形模式
- [ ] 张开手切换到球形模式
- [ ] 捏合进入聚焦模式
- [ ] 识别准确无误触发

**鼠标控制**：
- [ ] 左键拖拽旋转
- [ ] 右键拖拽平移
- [ ] 滚轮缩放
- [ ] 双击聚焦

**键盘快捷键**：
- [ ] H - 隐藏/显示 UI
- [ ] C - 切换摄像头
- [ ] M - 播放/暂停音乐
- [ ] N - 静音/取消静音
- [ ] P - 截图
- [ ] V - 录制视频
- [ ] 1/2/3 - 模式切换
- [ ] Esc - 退出聚焦

**文件上传**：
- [ ] 文件夹选择（Chrome/Edge）
- [ ] 文件多选
- [ ] 拖拽上传
- [ ] 自动压缩

**音频功能**：
- [ ] 自动播放
- [ ] 音量调节
- [ ] 静音功能
- [ ] 页面失焦暂停

**截图录制**：
- [ ] PNG 截图
- [ ] MP4 视频录制
- [ ] 文件正常下载

**浏览器兼容性**：
- [ ] Chrome 90+
- [ ] Firefox 88+
- [ ] Edge 90+
- [ ] Safari 15.4+

**性能测试**：
- [ ] FPS 监控准确
- [ ] 内存无泄漏
- [ ] 页面切换正常休眠

### 错误处理测试

- [ ] 图片加载失败提示
- [ ] 配置文件错误降级
- [ ] 手势识别失败降级
- [ ] 初始化失败友好提示

---

## 📄 Git Commit 规范

### Commit Message 格式

```
<类型>(<范围>): <简短描述>

<详细描述>（可选）

<Footer>（可选）
```

**类型**：
- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 重构
- `perf`: 性能优化
- `test`: 测试相关
- `chore`: 构建工具或辅助工具

**示例**：
```bash
feat(loader): 添加 WebP 格式支持

- 在 supportedExtensions 中添加 .webp
- 更新加载逻辑以支持 WebP
- 更新文档说明

Closes #123
```

---

## 🎯 开发优先级

### 高优先级
- 🐛 Bug 修复
- 🔒 安全问题
- 📚 文档完善
- ♿ 可访问性改进

### 中优先级
- ✨ 新功能
- ⚡ 性能优化
- 🎨 UI/UX 改进

### 低优先级
- 🧹 代码清理
- 📝 注释补充
- 🌐 多语言支持

---

## 💬 获取帮助

如果你在贡献过程中遇到问题：

1. 查看 [README.md](README.md) 和 [CHANGELOG.md](CHANGELOG.md)
2. 搜索现有的 Issues 和 Discussions
3. 创建新的 Issue 提问
4. 在 Pull Request 中提问

---

## 🙏 感谢

感谢你考虑为本项目做出贡献！每一个贡献，无论大小，都对项目有帮助。

**主要贡献者**：
- 项目创建者
- 文档贡献者
- Bug 报告者
- 功能建议者

---

**最后更新**：2025-12-07
**版本**：v3.0
