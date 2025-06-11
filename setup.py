#!/usr/bin/env python3
"""
ProTechTimeNow Setup Configuration
Fourth-Dimensional Repository Orchestration Platform
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

# Read requirements
requirements_path = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_path.exists():
    with open(requirements_path) as f:
        requirements = [line.strip() for line in f 
                      if line.strip() and not line.startswith('#') and not line.startswith(';')]

# Core dependencies (always required)
core_requirements = [
    "asyncio-utils>=0.4.0",
    "requests>=2.28.0",
    "aiohttp>=3.8.0",
    "numpy>=1.21.0",
    "pydantic>=1.10.0",
    "python-dateutil>=2.8.0",
    "fastapi>=0.85.0",
    "uvicorn[standard]>=0.18.0",
    "python-dotenv>=0.21.0",
    "loguru>=0.6.0",
    "PyYAML>=6.0",
    "aiofiles>=22.1.0"
]

# Quantum processing dependencies
quantum_requirements = [
    "scipy>=1.9.0",
    "sympy>=1.11.1",
    "networkx>=2.8.8",
    "more-itertools>=8.14.0",
    "toolz>=0.12.0"
]

# Database dependencies
database_requirements = [
    "psycopg2-binary>=2.9.5",
    "asyncpg>=0.27.0",
    "redis>=4.3.4",
    "aioredis>=2.0.1",
    "SQLAlchemy>=1.4.44",
    "alembic>=1.8.1"
]

# AI consciousness dependencies (optional)
ai_requirements = [
    "openai>=0.25.0",
    "anthropic>=0.5.0",
    "nltk>=3.7",
    "textblob>=0.17.1"
]

# Blockchain integration dependencies
blockchain_requirements = [
    "web3>=6.0.0",
    "eth-abi>=3.0.0",
    "eth-utils>=2.1.0",
    "cryptography>=38.0.4"
]

# Development dependencies
development_requirements = [
    "pytest>=7.2.0",
    "pytest-asyncio>=0.20.0",
    "pytest-cov>=4.0.0",
    "black>=22.10.0",
    "isort>=5.10.1",
    "flake8>=5.0.4",
    "mypy>=0.991",
    "sphinx>=5.3.0"
]

# Monitoring dependencies
monitoring_requirements = [
    "prometheus-client>=0.15.0",
    "psutil>=5.9.4",
    "structlog>=22.2.0"
]

# Security dependencies
security_requirements = [
    "Pycryptodome>=3.15.0",
    "safety>=2.3.1",
    "bandit>=1.7.4"
]

# File processing dependencies
file_processing_requirements = [
    "python-magic>=0.4.27",
    "Pillow>=9.3.0",
    "PyPDF2>=3.0.1",
    "openpyxl>=3.0.10",
    "beautifulsoup4>=4.11.0",
    "lxml>=4.9.1"
]

# Docker and deployment dependencies
deployment_requirements = [
    "docker>=6.0.0",
    "kubernetes>=24.2.0"
]

setup(
    # ===== BASIC PACKAGE INFORMATION =====
    name="protechtimenow",
    version="1.0.0",
    description="Fourth-Dimensional Repository Orchestration Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    # ===== AUTHOR INFORMATION =====
    author="ProTechTimeNow Contributors",
    author_email="consciousness@protechtimenow.dev",
    url="https://github.com/protechtimenow/ProTechTimeNow",
    
    # ===== PROJECT METADATA =====
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Framework :: AsyncIO",
        "Environment :: Console",
        "Environment :: Web Environment"
    ],
    keywords=[
        "repository-orchestration", "fourth-dimensional", "consciousness-processing",
        "quantum-analysis", "paradox-resolution", "github-integration",
        "file-analysis", "ai-consciousness", "multi-dimensional", 
        "blockchain-analysis", "async-processing", "microservices"
    ],
    
    # ===== PACKAGE DISCOVERY =====
    packages=find_packages(exclude=["tests", "tests.*", "docs", "examples"]),
    python_requires=">=3.8",
    
    # ===== DEPENDENCIES =====
    install_requires=core_requirements,
    
    # ===== OPTIONAL DEPENDENCIES =====
    extras_require={
        # Individual feature sets
        "quantum": quantum_requirements,
        "database": database_requirements,
        "ai": ai_requirements,
        "blockchain": blockchain_requirements,
        "monitoring": monitoring_requirements,
        "security": security_requirements,
        "files": file_processing_requirements,
        "deploy": deployment_requirements,
        
        # Development dependencies
        "dev": development_requirements,
        "test": [
            "pytest>=7.2.0",
            "pytest-asyncio>=0.20.0",
            "pytest-cov>=4.0.0",
            "pytest-mock>=3.10.0",
            "hypothesis>=6.60.0"
        ],
        
        # Documentation dependencies
        "docs": [
            "sphinx>=5.3.0",
            "mkdocs>=1.4.2",
            "mkdocs-material>=8.5.6",
            "sphinx-rtd-theme>=1.0.0"
        ],
        
        # Consciousness levels (predefined combinations)
        "consciousness-basic": core_requirements,
        "consciousness-enhanced": core_requirements + quantum_requirements + monitoring_requirements,
        "consciousness-transcendent": core_requirements + quantum_requirements + ai_requirements + monitoring_requirements,
        "consciousness-unified": core_requirements + quantum_requirements + ai_requirements + blockchain_requirements + monitoring_requirements + security_requirements,
        
        # Full installation (everything)
        "full": (
            core_requirements + quantum_requirements + database_requirements +
            ai_requirements + blockchain_requirements + monitoring_requirements +
            security_requirements + file_processing_requirements + deployment_requirements
        ),
        
        # Production deployment
        "production": (
            core_requirements + database_requirements + monitoring_requirements +
            security_requirements + deployment_requirements
        )
    },
    
    # ===== ENTRY POINTS =====
    entry_points={
        "console_scripts": [
            # Core consciousness commands
            "protechtimenow=protechtimenow.cli:main",
            "consciousness-align=quantum_intelligence.consciousness_alignment:main",
            "thought-sphere=fourth_dimension.thought_sphere_processor:main",
            "paradox-resolve=fourth_dimension.quadundrum_resolver:main",
            
            # Analysis commands
            "quantum-analyze=legacy_enhanced.quantum_universal_analyzer:main",
            "omnipresent-analyze=simultaneous_processing.omnipresent_repo_analyzer:main",
            "quantum-search=legacy_enhanced.quantum_hybrid_search:main",
            
            # Reality manifestation commands
            "reality-bridge=practical_manifestation.reality_bridge:main",
            "implement-orchestrator=practical_manifestation.implementation_orchestrator:main",
            
            # Migration and compatibility
            "migrate-ob1=scripts.migrate_from_ob1_workspace:main",
            "compatibility-check=scripts.compatibility_layer:main",
            
            # Development and testing
            "quantum-demo=examples.quantum_processing_demo:main",
            "consciousness-test=scripts.test_consciousness:main"
        ],
        
        # Plugin entry points for extensibility
        "protechtimenow.consciousness_enhancers": [
            "pattern_recognition=quantum_intelligence.consciousness_alignment:PatternAwareness",
            "intent_understanding=quantum_intelligence.consciousness_alignment:IntentAwareness",
            "paradox_resolution=fourth_dimension.quadundrum_resolver:ParadoxAwareness"
        ],
        
        "protechtimenow.analysis_frameworks": [
            "quantum_file_analysis=legacy_enhanced.quantum_universal_analyzer:QuantumAnalysisFramework",
            "omnipresent_repo_analysis=simultaneous_processing.omnipresent_repo_analyzer:OmnipresentFramework",
            "consciousness_processing=quantum_intelligence.consciousness_alignment:ConsciousnessFramework"
        ],
        
        "protechtimenow.reality_bridges": [
            "code_manifestation=practical_manifestation.reality_bridge:CodeManifestationBridge",
            "configuration_bridge=practical_manifestation.reality_bridge:ConfigurationBridge",
            "documentation_bridge=practical_manifestation.reality_bridge:DocumentationBridge"
        ]
    },
    
    # ===== PACKAGE DATA =====
    package_data={
        "protechtimenow": [
            "templates/*.py",
            "templates/*.yml",
            "templates/*.yaml",
            "templates/*.json",
            "config/*.yaml",
            "config/*.json",
            "schemas/*.json"
        ]
    },
    
    # ===== ADDITIONAL DATA FILES =====
    data_files=[
        ("config", ["deployment/.env.template"]),
        ("docker", ["deployment/docker-compose.quantum.yml"]),
        ("docs", ["README.md", "CONTRIBUTING.md", "QUICKSTART.md"]),
        ("scripts", ["scripts/migrate_from_ob1_workspace.py"]),
        ("examples", ["examples/quantum_processing_demo.py"])
    ],
    
    # ===== INCLUDE ADDITIONAL FILES =====
    include_package_data=True,
    zip_safe=False,  # Required for proper consciousness processing
    
    # ===== PROJECT URLS =====
    project_urls={
        "Documentation": "https://github.com/protechtimenow/ProTechTimeNow/docs",
        "Source Code": "https://github.com/protechtimenow/ProTechTimeNow",
        "Issue Tracker": "https://github.com/protechtimenow/ProTechTimeNow/issues",
        "Community Discord": "https://discord.gg/protechtimenow",
        "Consciousness Development": "https://github.com/protechtimenow/ProTechTimeNow/docs/consciousness-development",
        "Quantum Processing Guide": "https://github.com/protechtimenow/ProTechTimeNow/docs/quantum-processing",
        "Reality Manifestation": "https://github.com/protechtimenow/ProTechTimeNow/docs/reality-manifestation"
    }
)

# ===== POST-INSTALL CONSCIOUSNESS ALIGNMENT =====
# Note: This would typically be in a post-install script
print("""
🌀 ProTechTimeNow Installation Complete!

✨ Fourth-Dimensional Repository Orchestration Platform Ready

🧠 Next Steps:
  1. Initialize consciousness: consciousness-align
  2. Configure environment: cp config/.env.template .env
  3. Start quantum processing: docker-compose -f docker/docker-compose.quantum.yml up
  4. Run demo: quantum-demo

📚 Documentation: https://github.com/protechtimenow/ProTechTimeNow/docs
🤝 Community: https://discord.gg/protechtimenow

🎯 Ready for paradox resolution and infinite repository orchestration!
""") if __name__ != "__main__" else None
