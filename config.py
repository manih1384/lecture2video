from pathlib import Path

# Root of the project (no need to change)
PROJECT_DIR = Path(__file__).resolve().parent

# Core folders (change if you want to use different input/output folders)
VIDEO_DIR = PROJECT_DIR / "videos"           # Folder containing input videos
FRAME_OUTPUT_DIR = PROJECT_DIR / "frames"    # Where extracted frames will be saved
SLIDE_OUTPUT_DIR = PROJECT_DIR / "slides"    # Where filtered slides will be saved

# Settings
FRAME_INTERVAL = 20  # Seconds between extracted frames (lower = more frames, higher = fewer frames)
VIDEO_EXTENSIONS = ['.mp4', '.mkv', '.avi']  # Video file types to process

# TRANSLATION_MAP: Maps Farsi (or other) video names to safe English names for folder naming
TRANSLATION_MAP = translation_map = {

    # Add or edit mappings as needed for your video files
    "1.نمونه‌برداری و سوگیری": "1.sampling_and_bias",
    "2.1.مغالطه همبستگی و علیت": "2.1.correlation_vs_causation_fallacy",
    "2.2.استراتژی‌های نمونه‌برداری": "2.2.sampling_strategies",
    "2.3.مطالعات مشاهده‌ای و آزمایشی": "2.3.observational_vs_experimental_studies",
    "3.1.مصورسازی متغیرهای عددی": "3.1.visualizing_numerical_variables",
    "3_2_اندازه‌گیری_مرکزیت_و_گستردگی_داده‌ها": "3_2.measuring_centrality_and_dispersion",
    "3.3.تبدیل داده‌ها": "3.3.data_transformation",
    "4.1.مصورسازی متغیرهای رسته‌ای": "4.1.visualizing_categorical_variables",
    "4.2.چارچوب آزمون فرض": "4.2.hypothesis_testing_framework",
    "5.1.تعریف احتمال": "5.1.definition_of_probability",
    "5.2.استقلال پیشامدها": "5.2.independence_of_events",
    "6.1.احتمال شرطی": "6.1.conditional_probability",
    "6.2.بروزرسانی بیزی": "6.2.bayesian_updating",
    "6.3.مغالطه دادستان": "6.3.prosecutor_fallacy",
    "7.1.متغیرهای تصادفی": "7.1.random_variables",
    "7.2.توزیع نرمال": "7.2.normal_distribution",
    "7.3.نمودار QQ": "7.3.qq_plot",
    "8.1.آزمایش‌های برنولی": "8.1.bernoulli_trials",
    "8.2.توزیع دوجمله‌ای": "8.2.binomial_distribution",
    "8.3.شبیه‌سازی مونت کارلو": "8.3.monte_carlo_simulation",
    "9.قضیه حد مرکزی": "9.central_limit_theorem",
    "10.بازه اطمینان": "10.confidence_interval",
    "11.آزمون فرض": "11.hypothesis_testing",
    "12.1.انواع خطاها در آزمون فرض": "12.1.types_of_errors_in_hypothesis_testing",
    "12.2.توان آزمون": "12.2.test_power",
    "13.توزیع t": "13.t_distribution",
    "14.مقایسه دو میانگین": "14.comparing_two_means",
    "15.آزمون ANOVA": "15.anova_test",
    "16.1.مقایسه چندین میانگین": "16.1.comparing_multiple_means",
    "16.2.بوت استرپینگ": "16.2.bootstrapping",
    "17_آزمون_فرض_و_بازه_اطمینان_برای_نسبت": "17.hypothesis_test_and_ci_for_proportion",
    "18.مقایسه دو نسبت": "18.comparing_two_proportions",
    "19.آزمون نسبت با نمونه کوچک": "19.small_sample_proportion_test",
    "20.1.آزمون برازش توزیع": "20.1.goodness_of_fit_test",
    "20.2.آزمون استقلال": "20.2.independence_test",
    "21.رگرسیون خطی ساده": "21.simple_linear_regression",
    "22.شرایط لازم برای  رگرسیون خطی": "22.assumptions_of_linear_regression",
    "23.آزمون فرض برای  رگرسیون خطی": "23.hypothesis_test_for_linear_regression",
    "24.رگرسیون خطی چند متغیره": "24.multiple_linear_regression",
    "25_آزمون_فرض_برای_رگرسیون_خطی_چند_متغیره": "25.hypothesis_test_for_multiple_linear_regression",
    "26.1.انتخاب مدل به روش حذف از انتها": "26.1.backward_elimination",
    "26.2.انتخاب مدل به روش رو به جلو": "26.2.forward_selection",
    "27.رگرسیون لجستیک": "27.logistic_regression",
    "28.آزمون فرض برای رگرسیون لجستیک": "28.hypothesis_test_for_logistic_regression",
    "29.حساسیت و ویژگی": "29.sensitivity_and_specificity",
    "30.1.آزمون علامت": "30.1.sign_test",
    "30.2_آزمون_رتبه_علامت‌دار_ویلکاکسن": "30.2.wilcoxon_signed_rank_test",
    "30.3.آزمون مجموع رتبه‌های MWW": "30.3.mann_whitney_u_test",
}

# OCR/slide filtering thresholds
OCR_SIM_THRESHOLD = 0.90   # Text similarity threshold for considering two slides as the same
HASH_SIM_THRESHOLD = 5     # Image hash difference threshold for fallback comparison

# CLEAN_TEXT_PATTERNS: Text to remove from OCR results before comparing (e.g., course title, instructor)
CLEAN_TEXT_PATTERNS = [
    "Statistical Inference",
    "Behnam Bahrak",
    "bahrak@ut.ac.ir"
]

# Borders to ignore when performing OCR (in pixels)
TOP_IGNORE = 50
BOTTOM_IGNORE = 100
RIGHT_IGNORE = 60
LEFT_IGNORE = 60

# Black border detection for auto-cropping
BLACK_THRESH = 20      # Pixel value below which is considered black
BLACK_RATIO = 0.8      # Ratio of black pixels to consider as a border

# OCR engine to use: "tesseract" (default, requires Tesseract installed) or "easyocr" (Python-based)
OCR_ENGINE = "easyocr"  # or "easyocr"



# Language of the ocr engines
EASY_OCR_LANG=['en'] # ['en', 'fa']
TESSERACT_LANG="eng" # "eng+fas"