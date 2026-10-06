# --- Boilerplate ---
# Setup:
#   pip install requests pillow colorama
#   config.py -> HF_API_KEY="hf_..."
#
# What it does:
#   1) Takes image path input
#   2) Calls HF Router chat completions with a VISION model to get 1-sentence caption
#   3) Uses TEXT models to rewrite that caption into:
#        - 5 words (caption)
#        - 30 words (description)
#        - 50 words (summary)
#   4) Falls back across model lists if one fails
#
# Key parts:
#   _data_url(path)         -> image file -> base64 data URL
#   query_hf_api(payload)   -> POST to https://router.huggingface.co/v1/chat/completions with error handling
#   _run_models(models,...) -> try models in order until a valid response
#   generate_exact_sentence -> retries + truncates to EXACT word count, ensures period
#   get_basic_caption       -> builds multimodal message (text + image_url) and returns caption or [Error]
#
# CLI flow:
#   - Generate basic caption once
#   - Menu loop: 1/2/3 produce outputs, 4 exits
#   - If caption failed, auto-retry caption when user selects 1/2/3
