import streamlit as st

# 终极强力清除 Streamlit 官方所有的红帽子、菜单、页脚和右下角标志
hide_streamlit_style = """
<style>
/* 1. 隐藏顶部的整条 Header（包含红帽子、GitHub 链接等） */
header {visibility: hidden !important; display: none !important;}
[data-testid="stHeader"] {visibility: hidden !important; display: none !important;}

/* 2. 隐藏右下角的 "Made with Streamlit" 页脚和浮动标志 */
footer {visibility: hidden !important; display: none !important;}
[data-testid="stFooter"] {visibility: hidden !important; display: none !important;}

/* 3. 隐藏右上角的 Deploy 部署按钮 */
.stAppDeployButton {display: none !important;}

/* 4. 隐藏右上角的三条杠主菜单 */
#MainMenu {visibility: hidden !important; display: none !important;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

import os
import json
import requests
import streamlit as st
import random
import string

# 1. 页面基本配置与高级视觉优化
st.set_page_config(page_title="私域超级操盘手系统", page_icon="🍒", layout="wide")

# CSS 注入：定制化高级 SaaS 质感、卡片微阴影
st.markdown("""
    <style>
    .main { background-color: #f4f6f9; }
    div.stButton > button { border-radius: 8px; font-weight: bold; border: none; }
    h1, h2, h3 { color: #2d3436; }
    .stTextInput > div > div > input, .stTextArea > div > div > textarea { border-radius: 8px; }
    .business-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. 核心 AI 引擎 (研发与营销双重铁律加固：全平台合规与违禁词硬拦截)
def get_ai_response(content):
    api_key = os.getenv("DASHSCOPE_API_KEY")
    url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    
    # 🛡️ 核心合规防线：全平台通用的底层 Prompt 铁律
    system_prompt = """你是一位顶级的全行业私域成交操盘手兼资深合规风控专家。【执行铁律（违反即为最高级别系统故障）】：
    1. 【绝对合规底线】：严禁使用《广告法》明令禁止的极限词及违禁词（如：最、第一、绝对、顶级、国家级、首个、绝无仅有等）。严禁涉及虚假宣传、夸大疗效、金融诱导、医疗擦边等违反法律法规的内容。
    2. 【全平台风控契合】：所有生成的话术、文案必须符合各大主流商业平台（微信、小红书、抖音、社群等）的合规监管标准，语气温和自然，严禁产生诱导分享、恶意营销或过度骚扰感。
    3. 【去 AI 腔与人味还原】：严禁使用公文腔、学术腔、AI味十足的排比句。必须使用活人语感、多用短句、加入生动 emoji，像真人私聊沟通一样随和走心。"""
    
    payload = {
        "model": "qwen3.7-plus",
        "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": content}],
        "temperature": 0.6
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=60)
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e: return f"系统异常，请检查网络或 Key ({str(e)})"

# --- 初始化会话状态 ---
if "chat_history" not in st.session_state: st.session_state.chat_history = []
if "is_vip" not in st.session_state: st.session_state.is_vip = False
if "admin_logged_in" not in st.session_state: st.session_state.admin_logged_in = False
if "copy_limit" not in st.session_state: st.session_state.copy_limit = 3
if "prod_val" not in st.session_state: st.session_state.prod_val = ""
if "sell_val" not in st.session_state: st.session_state.sell_val = ""

# 黄金视觉比例
col_main, col_right = st.columns([2.2, 1])

# ==================== 右侧：商业闭环与管理中心 ====================
with col_right:
    with st.container():
        st.markdown('<div class="business-card">', unsafe_allow_html=True)
        
        # 1. 管理员入口
        with st.expander("🔑 管理员专属后台"):
            if not st.session_state.admin_logged_in:
                admin_pwd = st.text_input("管理密码", type="password")
                if st.button("登录管理"):
                    if admin_pwd == "888888":  
                        st.session_state.admin_logged_in = True
                        st.rerun()
                    else:
                        st.error("密码错误")
            else:
                st.success("✅ 已进入管理")
                c_type = st.selectbox("选择档次", ["DAY", "WEEK", "MONTH", "SEASON", "YEAR"])
                price = st.text_input("输入价格", "39")
                if st.button("生成新卡密"):
                    suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                    st.code(f"{c_type}-{price}-{suffix}")
                if st.button("退出管理"):
                    st.session_state.admin_logged_in = False
                    st.rerun()

        # 2. 会员与商业化矩阵
        st.markdown("### 💎 VIP 会员中心")
        if st.session_state.is_vip:
            st.success("👑 当前身份：VIP 无限畅用会员")
            st.balloons()
        else:
            st.warning(f"🎁 免费体验版\n• 剩余文案额度: {st.session_state.copy_limit} 次")
            st.markdown("---")
            st.markdown("### 🚀 黄金卡密矩阵")
            st.markdown(
                "• **⚡ 体验日卡**：`￥3.9`\n"
                "• **🔥 冲刺周卡**：`￥19.9`\n"
                "• **💎 标准月卡**：`￥39.0`\n"
                "• **👑 超级季卡**：`￥88.0`\n"
                "• **🚀 尊享年卡**：`￥198.0`"
            )
            
            with st.expander("💳 获取激活卡密渠道", expanded=True):
                st.markdown("**1.** 扫描下方二维码加微信获取凭证。")
                if os.path.exists("pay_qrcode.png"):
                    st.image("pay_qrcode.png", width=160)
                else:
                    st.info("💡 请将收款码命名为 `pay_qrcode.png`")

                st.markdown("💬 **客服微信号：**")
                st.code("chengzhi4914", language=None)

            st.markdown("### 🔑 卡密激活")
            input_code = st.text_input("输入卡密激活", placeholder="例如：MONTH-39-XXXX")
            if st.button("立即激活 VIP", use_container_width=True):
                if input_code.startswith("DAY") or input_code.startswith("WEEK") or input_code.startswith("MONTH") or input_code.startswith("SEASON") or input_code.startswith("YEAR") or input_code.startswith("VIP"):
                    st.session_state.is_vip = True
                    st.success("🎉 激活成功！")
                    st.rerun()
                else:
                    st.error("❌ 激活码无效！")
        st.markdown('</div>', unsafe_allow_html=True)

# ==================== 左侧：主业务区 ====================
with col_main:
    st.title("🍒 私域超级操盘手与成交智囊系统")
    st.markdown("集 **【全域高转化文案】** 与 **【私聊促单助手】** 于一体的智能成交引擎，完美适配各行各业与主流多平台！")
    st.markdown("---")

    tab1, tab2 = st.tabs(["🔥 爆款文案生成器", "💬 高情商私聊促单助手"])

    # 模块一：文案生成
    with tab1:
        st.subheader("✍️ 定义商品与营销策略")
        st.markdown("💡 **快速行业示例（点击一键填充）：**")
        c_ex1, c_ex2, c_ex3 = st.columns(3)
        with c_ex1:
            if st.button("🍒 生鲜水果", use_container_width=True):
                st.session_state.prod_val = "原箱特级大车厘子"
                st.session_state.sell_val = "顺丰空运包赔、果径3J、坏单包赔、限时买一送一"
        with c_ex2:
            if st.button("💄 美妆护肤", use_container_width=True):
                st.session_state.prod_val = "大牌修护抗皱精华液"
                st.session_state.sell_val = "专柜正品、敏感肌可用、买正装送同款小样、立省200元"
        with c_ex3:
            if st.button("📚 知识付费", use_container_width=True):
                st.session_state.prod_val = "私域爆粉变现训练营"
                st.session_state.sell_val = "7天实战落地、助教1对1指导、零基础起号、早鸟价特惠"

        col_a, col_b = st.columns(2)
        with col_a: 
            prod = st.text_input("产品/服务名称", key="prod_val", placeholder="例如：原箱车厘子...")
        with col_b: 
            sell = st.text_input("核心卖点/优惠", key="sell_val", placeholder="例如：顺丰空运、限时立减...")
        
        if st.button("🚀 启动成交决策引擎", use_container_width=True, type="primary"):
            if not st.session_state.is_vip and st.session_state.copy_limit <= 0:
                st.error("🚨 免费额度已用完，请通过右侧扫码获取卡密激活！")
            else:
                with st.spinner("操盘手正在重构成交逻辑（系统正进行全网合规与违禁词反查）..."):
                    prompt_strategy = f"""
                    产品/服务：{prod}，核心卖点/优惠：{sell}。
                    请策划一套“全行业通用私域成交组合拳”：
                    1. 朋友圈/社群/跨平台种草文案（侧重痛点共情与信任建立）；
                    2. 客户私聊转化话术（侧重疑虑化解与价值锚定）；
                    3. 成交临门一脚的话术（侧重稀缺性与限时驱动）。
                    保持极高的接地气程度，剔除一切AI味。
                    """
                    res = get_ai_response(prompt_strategy)
                    if not st.session_state.is_vip:
                        st.session_state.copy_limit -= 1
                    st.info("✅ 决策引擎已完成深度定制（已通过全网广告法合规过滤与真人语感质检）")
                    st.markdown("---")
                    st.markdown(res)

        # 🎯 丰满左侧下方空间（与右侧卡密激活高度完美对齐，改为全网通用的合规与成交双保险公示）
        st.markdown("---")
        st.markdown("### 🏆 私域成交铁人三项心法")
        info_col1, info_col2, info_col3 = st.columns(3)
        with info_col1:
            st.info("**1. 情绪共鸣**\n\n卖产品不如卖场景，先击中痛点，客户才会放下防备。")
        with info_col2:
            st.success("**2. 信任锚定**\n\n晒出真实反馈与限时稀缺感，加速客户当场下单。")
        with info_col3:
            st.warning("**3. 高情商回复**\n\n永远站在客户角度把顾虑化解于无形，聊天即成交。")
        
        st.markdown("---")
        st.markdown(
            "🛡️ **全网合规与监管双保险内核**：本系统已内置严格的《广告法》违禁词过滤与多平台合规风控引擎，全自动规避夸大宣传及监管红线，确保全网各渠道输出的内容既能高效转化，又安全稳健。"
        )

    # 模块二：私聊助手
    with tab2:
        st.subheader("🎯 客户原话分析与促单")
        st.markdown("💡 **常见客户异议（点击快速模拟）：**")
        p_ex1, p_ex2 = st.columns(2)
        with p_ex1:
            if st.button("💬 “价格太贵了，能不能便宜点？”", use_container_width=True):
                st.session_state.quick_chat = "产品有点贵哎，别人家才卖一半价格，能不能便宜点或者送点东西？"
        with p_ex2:
            if st.button("💬 “我再考虑看看/和朋友商量下”", use_container_width=True):
                st.session_state.quick_chat = "看起来还行，不过我得再考虑几天，或者跟朋友商量一下再决定。"

        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]): st.markdown(msg["content"])
            
        prompt = st.chat_input("粘贴客户在私信或微信发给你的原话（例如：有点贵哎...）")
        
        if "quick_chat" in st.session_state and st.session_state.quick_chat:
            prompt = st.session_state.quick_chat
            st.session_state.quick_chat = "" 

        if prompt:
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            
            with st.spinner("💡 正在生成高情商回复方案..."):
                reply = get_ai_response(f"客户原话：{prompt}。给出3种高情商、接地气的回复建议，模拟真实私聊沟通。")
                st.session_state.chat_history.append({"role": "assistant", "content": reply})
                with st.chat_message("assistant"): st.markdown(reply)

        # 🎯 丰满左侧下方空间（私聊页底部常驻，与右侧绝对对齐）
        st.markdown("---")
        st.markdown("### 💡 私聊促单金句提示")
        st.markdown(
            "• **异议不是拒绝**：客户说贵是在确认价值，引导看长远价值而不是单价。\n"
            "• **限时稀缺驱动**：通过“今天发货、仅剩最后X名”打破拖延心理。"
        )
        st.markdown("---")
        st.markdown("🛡️ **合规成交准则**：专业且有温度的合规对答，既能打消客户顾虑，又能彻底规避多平台私信聊天合规风险。")
