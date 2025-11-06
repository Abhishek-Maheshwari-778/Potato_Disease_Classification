# 🤝 Contributing to Potato Disease Classification

Thank you for your interest in contributing to the Potato Disease Classification project! We welcome contributions from the community.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Git
- Basic knowledge of Machine Learning and Web Development

### Development Setup
1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Potato_Disease_Classification.git
   cd Potato_Disease_Classification
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate  # Windows
   ```

4. Install dependencies:
   ```bash
   cd api && pip install -r requirements.txt && cd ..
   cd website && pip install -r requirements.txt && cd ..
   ```

## 📝 Types of Contributions

### 🐛 Bug Reports
- Use the [GitHub Issues](https://github.com/Abhishek-Maheshwari-778/Potato_Disease_Classification/issues) page
- Include steps to reproduce
- Add screenshots if applicable
- Specify your environment (OS, Python version, etc.)

### 💡 Feature Requests
- Open an issue with the `enhancement` label
- Describe the feature and its benefits
- Provide examples of how it would work

### 🔧 Code Contributions
- **Model Improvements**: Better architectures, hyperparameter tuning
- **UI/UX Enhancements**: Better Streamlit interface, responsive design
- **API Features**: New endpoints, better error handling
- **Documentation**: Tutorials, better examples, translations
- **Testing**: Unit tests, integration tests

### 📊 Data Contributions
- **Dataset Expansion**: More potato leaf images
- **Data Augmentation**: Improved training data
- **Annotation**: Better labeling and categorization

## 🔄 Development Workflow

### 1. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

### 2. Make Your Changes
- Follow the existing code style
- Add comments for complex logic
- Update documentation as needed
- Test your changes thoroughly

### 3. Commit Your Changes
```bash
git add .
git commit -m "feat: add new feature description"
# or
git commit -m "fix: resolve issue with..."
```

Use conventional commit messages:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation
- `style:` for formatting
- `refactor:` for code refactoring
- `test:` for tests
- `chore:` for maintenance

### 4. Push and Create Pull Request
```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:
- Clear title and description
- Reference to any related issues
- Screenshots/demo if applicable

## 🎯 Areas for Contribution

### High Priority
- [ ] **Model Performance**: Improve accuracy beyond 95%
- [ ] **Mobile App**: React Native or Flutter mobile application
- [ ] **Real-time Processing**: Webcam integration for live detection
- [ ] **Multi-language Support**: Interface in multiple languages

### Medium Priority
- [ ] **Docker Support**: Containerize the application
- [ ] **Cloud Deployment**: AWS/GCP/Azure deployment scripts
- [ ] **Batch Processing**: Handle multiple images at once
- [ ] **API Rate Limiting**: Implement request throttling

### Low Priority
- [ ] **Dark Mode**: Theme switching capability
- [ ] **Export Results**: PDF/CSV export functionality
- [ ] **User Authentication**: Login and user management
- [ ] **Analytics Dashboard**: Usage statistics and insights

## 🧪 Testing Guidelines

### Before Submitting
- [ ] Test the application locally
- [ ] Verify API endpoints work correctly
- [ ] Check that the Streamlit interface functions properly
- [ ] Test with different image formats (JPG, PNG, JPEG)
- [ ] Verify error handling works as expected

### Running Tests
```bash
# Start the backend
cd api && python main.py

# In another terminal, test the frontend
cd website && streamlit run app.py

# Test API endpoints
curl -X GET http://localhost:8000/ping
```

## 📋 Pull Request Checklist

- [ ] Code follows the project's style guidelines
- [ ] Self-review of code completed
- [ ] Comments added for complex logic
- [ ] Documentation updated (if needed)
- [ ] No breaking changes (or properly documented)
- [ ] Tests pass locally
- [ ] Related issues referenced
- [ ] Screenshots added (for UI changes)

## 🏷️ Issue Labels

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested

## 💬 Communication

- **Issues**: For bug reports and feature requests
- **Discussions**: For questions and general discussion
- **Email**: abhishek.maheshwari@example.com

## 🎉 Recognition

Contributors will be:
- Added to the contributors list
- Mentioned in release notes
- Given credit in the README

Thank you for contributing to make this project better! 🌟