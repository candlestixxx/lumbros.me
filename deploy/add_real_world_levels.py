"""
Script to inject:
INTERACTIVE REAL-WORLD TECH LEVELS // LIFE ERRANDS & DAILY LOGISTICS
Levels 01 - 04:
- Level 01: Going to the Bank & Liquidity Run
- Level 02: Local Brand Name Grocery Store & Interactive Weekly Deals Flyer
- Level 03: Pharmacy, Wellness & Utilities Optimization
- Level 04: Master Real-World Harmony & Freedom Status

Strict adherence to WordPress entity safety: ZERO raw '&&' inside script tags.
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOMEPAGE_PATH = os.path.join(BASE_DIR, 'homepage.html')

with open(HOMEPAGE_PATH, 'r', encoding='utf-8') as f:
    home = f.read()

REAL_WORLD_LEVELS_HTML = '''
      <!-- =========================================================================
           PART 2.5: INTERACTIVE REAL-WORLD TECH LEVELS // LIFE ERRANDS & LOGISTICS
           FROM STEP 1 TO REAL-WORLD INTERACTION: GOING TO THE BANK & LOCAL BRAND GROCERY STORES
           WITH LIVE WEEKLY DEALS, DIGITAL CLIPPABLE COUPONS & SMART CASHFLOW
           ========================================================================= -->
      <div class="real-world-levels-wrapper" id="real-world-levels-experience" style="margin-top: 35px; border-top: 2px solid rgba(0,255,102,0.35); padding-top: 30px;">
        
        <div style="text-align: center; margin-bottom: 22px;">
          <div style="display: inline-block; background: rgba(0,255,102,0.12); border: 1px solid #00ff66; padding: 4px 14px; border-radius: 4px; font-size: 0.75rem; font-weight: 800; color: #00ff66; letter-spacing: 2px; margin-bottom: 8px;">
            ⟬ INTERACTIVE REAL-WORLD LEVELS // PLAYABLE DIGITAL LIFE TECH ⟭
          </div>
          <h3 style="color: #ffffff; font-size: 1.35rem; font-weight: 800; margin: 0 0 8px 0; letter-spacing: 1px;">
            LEVELS 01 - 04: GOING TO THE BANK &amp; LOCAL BRAND GROCERY STORES WITH WEEKLY DEALS
          </h3>
          <p style="color: #8ce4a7; font-size: 0.8rem; max-width: 880px; margin: 0 auto; line-height: 1.5;">
            Step into real-world daily logistics. Experience hands-on interactive levels just like the calibration steps from Step 1: Manage cashflow at the <strong>Bank &amp; ATM</strong>, navigate your favorite <strong>Brand-Name Grocery Store</strong> (Kroger, Trader Joe's, Aldi, Whole Foods), clip <strong>real weekly circular deals</strong>, scan coupons at checkout, and protect your family&rsquo;s health and wallet.
          </p>
        </div>

        <!-- Level Sequential Stepper Tabs Rail (Like Step 1, 2, 3) -->
        <div class="level-stepper-rail" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 8px; margin-bottom: 22px;">
          
          <button type="button" class="level-step-btn active" data-level="1" id="level-step-btn-1" style="background: rgba(0,255,102,0.15); border: 1px solid #00ff66; border-radius: 6px; padding: 10px 12px; text-align: left; cursor: pointer; transition: all 0.2s ease;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px;">
              <span style="background: #00ff66; color: #02070f; font-size: 0.65rem; font-weight: 900; padding: 2px 6px; border-radius: 3px;">LEVEL 01</span>
              <span style="font-size: 0.68rem; color: #00ff66; font-weight: 800;">ACTIVE</span>
            </div>
            <div style="color: #ffffff; font-size: 0.82rem; font-weight: 800;">GOING TO THE BANK</div>
            <div style="font-size: 0.68rem; color: #8ce4a7;">Liquidity Run &bull; ATM &bull; Debt vs Savings</div>
          </button>

          <button type="button" class="level-step-btn" data-level="2" id="level-step-btn-2" style="background: rgba(5,15,25,0.7); border: 1px solid rgba(0,229,255,0.3); border-radius: 6px; padding: 10px 12px; text-align: left; cursor: pointer; transition: all 0.2s ease;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px;">
              <span style="background: #00e5ff; color: #02070f; font-size: 0.65rem; font-weight: 900; padding: 2px 6px; border-radius: 3px;">LEVEL 02</span>
              <span style="font-size: 0.68rem; color: #8ce4a7;">FEATURED</span>
            </div>
            <div style="color: #ffffff; font-size: 0.82rem; font-weight: 800;">LOCAL BRAND GROCERY STORE</div>
            <div style="font-size: 0.68rem; color: #8ce4a7;">Weekly Deals Flyer &bull; Cart &bull; Coupons</div>
          </button>

          <button type="button" class="level-step-btn" data-level="3" id="level-step-btn-3" style="background: rgba(5,15,25,0.7); border: 1px solid rgba(0,229,255,0.3); border-radius: 6px; padding: 10px 12px; text-align: left; cursor: pointer; transition: all 0.2s ease;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px;">
              <span style="background: #d500f9; color: #ffffff; font-size: 0.65rem; font-weight: 900; padding: 2px 6px; border-radius: 3px;">LEVEL 03</span>
              <span style="font-size: 0.68rem; color: #8ce4a7;">HEALTH &amp; HOMELAND</span>
            </div>
            <div style="color: #ffffff; font-size: 0.82rem; font-weight: 800;">PHARMACY &amp; UTILITIES</div>
            <div style="font-size: 0.68rem; color: #8ce4a7;">Prescriptions &bull; Bill Negotiations</div>
          </button>

          <button type="button" class="level-step-btn" data-level="4" id="level-step-btn-4" style="background: rgba(5,15,25,0.7); border: 1px solid rgba(0,229,255,0.3); border-radius: 6px; padding: 10px 12px; text-align: left; cursor: pointer; transition: all 0.2s ease;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px;">
              <span style="background: #ffaa00; color: #02070f; font-size: 0.65rem; font-weight: 900; padding: 2px 6px; border-radius: 3px;">LEVEL 04</span>
              <span style="font-size: 0.68rem; color: #8ce4a7;">MASTERY</span>
            </div>
            <div style="color: #ffffff; font-size: 0.82rem; font-weight: 800;">MASTER FREEDOM STATUS</div>
            <div style="font-size: 0.68rem; color: #8ce4a7;">532nm Planetary Harmony &bull; Trophy</div>
          </button>

        </div>


        <!-- ===================================================================
             LEVEL 01 DISPLAY CONTAINER: GOING TO THE BANK & ATM LIQUIDITY RUN
             =================================================================== -->
        <div class="level-content-pane" id="level-pane-1" style="display: block; background: rgba(3,12,22,0.9); border: 1px solid rgba(0,255,102,0.35); border-radius: 8px; padding: 20px; box-shadow: 0 0 25px rgba(0,255,102,0.08); margin-bottom: 25px;">
          
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(0,255,102,0.25); padding-bottom: 12px; margin-bottom: 16px; flex-wrap: wrap; gap: 10px;">
            <div>
              <span style="background: #00ff66; color: #030a12; font-weight: 900; font-size: 0.72rem; padding: 2px 8px; border-radius: 3px;">LEVEL 01 ARENA</span>
              <span style="color: #ffffff; font-weight: 800; font-size: 1.05rem; margin-left: 10px; letter-spacing: 1px;">GOING TO THE BANK // REAL LIQUIDITY &amp; WEALTH CONSOLE</span>
            </div>
            
            <!-- Bank Institution Selector -->
            <div style="display: flex; align-items: center; gap: 8px;">
              <span style="font-size: 0.7rem; color: #8ce4a7; font-weight: 700;">INSTITUTION:</span>
              <select id="bank-institution-select" style="background: #01060d; color: #00ff66; border: 1px solid rgba(0,255,102,0.4); font-size: 0.72rem; padding: 4px 10px; border-radius: 4px; font-weight: 700; cursor: pointer;">
                <option value="chase" selected>🏦 Chase / Tier-1 Commercial Bank</option>
                <option value="credit_union">🏛️ First Community Credit Union (0 Fees, High Trust)</option>
                <option value="sovereign_defi">⚡ High-Yield Sovereign Treasury (4.85% APY)</option>
              </select>
            </div>
          </div>

          <!-- Real-Time Bank Account Cards Grid -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 12px; margin-bottom: 18px;">
            
            <div style="background: rgba(5,16,28,0.8); border: 1px solid rgba(0,229,255,0.3); border-radius: 6px; padding: 12px;">
              <div style="font-size: 0.68rem; color: #8ce4a7; margin-bottom: 2px;">CHECKING ACCOUNT (OPERATING CASH):</div>
              <div id="bank-checking-val" style="font-size: 1.25rem; font-weight: 900; color: #00e5ff; font-family: 'Share Tech Mono', monospace;">$1,420.00</div>
              <div style="font-size: 0.65rem; color: #b8e2c8; margin-top: 4px;">Available on Debit Card &bull; Paycheck destination</div>
            </div>

            <div style="background: rgba(5,16,28,0.8); border: 1px solid rgba(0,255,102,0.3); border-radius: 6px; padding: 12px;">
              <div style="font-size: 0.68rem; color: #8ce4a7; margin-bottom: 2px;">HIGH-YIELD SAVINGS (EMERGENCY RESERVE):</div>
              <div id="bank-savings-val" style="font-size: 1.25rem; font-weight: 900; color: #00ff66; font-family: 'Share Tech Mono', monospace;">$5,800.00</div>
              <div style="font-size: 0.65rem; color: #b8e2c8; margin-top: 4px;">Earning +$23.40/mo at 4.85% APY compounding</div>
            </div>

            <div style="background: rgba(5,16,28,0.8); border: 1px solid rgba(255,80,80,0.3); border-radius: 6px; padding: 12px;">
              <div style="font-size: 0.68rem; color: #ff8888; margin-bottom: 2px;">REVOLVING CREDIT CARD (24.9% APR):</div>
              <div id="bank-debt-val" style="font-size: 1.25rem; font-weight: 900; color: #ff5555; font-family: 'Share Tech Mono', monospace;">-$1,650.00</div>
              <div style="font-size: 0.65rem; color: #ffaaaa; margin-top: 4px;">Min payment: $65/mo &bull; Interest cost: $34.20/mo</div>
            </div>

            <div style="background: rgba(5,16,28,0.8); border: 1px solid rgba(255,170,0,0.3); border-radius: 6px; padding: 12px;">
              <div style="font-size: 0.68rem; color: #ffaa00; margin-bottom: 2px;">FINANCIAL FREEDOM RUNWAY:</div>
              <div id="bank-runway-val" style="font-size: 1.25rem; font-weight: 900; color: #ffaa00; font-family: 'Share Tech Mono', monospace;">3.6 MONTHS</div>
              <div style="font-size: 0.65rem; color: #ffd680; margin-top: 4px;">Based on $2,000/mo baseline living expenses</div>
            </div>

          </div>

          <!-- Interactive Banking Situation Deck -->
          <div style="background: rgba(8,20,32,0.9); border: 1px solid rgba(0,255,102,0.25); border-radius: 6px; padding: 16px; margin-bottom: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
              <span style="color: #00ff66; font-size: 0.72rem; font-weight: 800; letter-spacing: 1px;">
                LIVE BANKING SCENARIO // PAYCHECK DEPOSIT ARRIVAL
              </span>
              <span style="font-size: 0.7rem; color: #8ce4a7; font-family: 'Share Tech Mono', monospace;">TRANSACTION: #BK-7894</span>
            </div>
            
            <h4 style="color: #ffffff; font-size: 0.95rem; font-weight: 800; margin: 0 0 6px 0;">
              Bi-Weekly Paycheck Direct Deposit Cleared: +$2,850.00
            </h4>
            <p style="color: #b8e2c8; font-size: 0.78rem; line-height: 1.5; margin: 0 0 14px 0;">
              Your bi-weekly paycheck of $2,850 has arrived at the bank. You have a high-interest credit card balance of $1,650 charging 24.9% APR ($34/mo in dead interest), upcoming rent/mortgage due in 5 days ($1,200), and grocery shopping planned this weekend. How will you allocate this liquidity?
            </p>

            <div class="bank-actions-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 10px;">
              <button type="button" class="bank-action-btn" id="btn-bank-kill-debt" style="background: rgba(0,255,102,0.12); border: 1px solid #00ff66; color: #ffffff; padding: 10px 14px; border-radius: 5px; font-size: 0.75rem; font-weight: 700; text-align: left; cursor: pointer; transition: all 0.2s ease;">
                <div style="color: #00ff66; font-weight: 900; margin-bottom: 2px;">⚡ ACTION 1: WIPE OUT CREDIT CARD IN FULL (-$1,650)</div>
                <div style="font-size: 0.68rem; color: #b8e2c8;">Eliminates all high-interest bleed, leaves $1,200 for rent + $1,420 checking cushion. (+Debt Freedom, +Credit Score)</div>
              </button>

              <button type="button" class="bank-action-btn" id="btn-bank-split-strategy" style="background: rgba(0,229,255,0.12); border: 1px solid #00e5ff; color: #ffffff; padding: 10px 14px; border-radius: 5px; font-size: 0.75rem; font-weight: 700; text-align: left; cursor: pointer; transition: all 0.2s ease;">
                <div style="color: #00e5ff; font-weight: 900; margin-bottom: 2px;">⚖️ ACTION 2: BALANCED 50/50 STRATEGY</div>
                <div style="font-size: 0.68rem; color: #b8e2c8;">Pay $1,000 toward credit card, deposit $1,000 into 4.85% High-Yield Savings, hold $850 for groceries. (+Reserves)</div>
              </button>

              <button type="button" class="bank-action-btn" id="btn-bank-ai-dispute" style="background: rgba(255,170,0,0.12); border: 1px solid #ffaa00; color: #ffffff; padding: 10px 14px; border-radius: 5px; font-size: 0.75rem; font-weight: 700; text-align: left; cursor: pointer; transition: all 0.2s ease;">
                <div style="color: #ffaa00; font-weight: 900; margin-bottom: 2px;">🛡️ ACTION 3: DEPLOY AI FINANCIAL NEGOTIATOR</div>
                <div style="font-size: 0.68rem; color: #b8e2c8;">Dispute $35 maintenance fee, negotiate credit APR down to 14.5%, and lock 5% APY savings rate. (+Leverage)</div>
              </button>
            </div>
          </div>

          <!-- Live Bank Terminal Log -->
          <div id="bank-terminal-feed" style="font-family: 'Share Tech Mono', monospace; font-size: 0.7rem; color: #8ce4a7; background: #010408; padding: 8px 12px; border-radius: 4px; border: 1px solid rgba(0,255,102,0.2);">
            ⟦ BANK ATM TERMINAL ⟧ Connected to secure core. Paycheck direct deposit verified. Ready for liquidity decision...
          </div>

        </div>


        <!-- ===================================================================
             LEVEL 02 DISPLAY CONTAINER: LOCAL BRAND NAME GROCERY STORE & WEEKLY DEALS
             =================================================================== -->
        <div class="level-content-pane" id="level-pane-2" style="display: none; background: rgba(3,12,22,0.9); border: 1px solid rgba(0,229,255,0.35); border-radius: 8px; padding: 20px; box-shadow: 0 0 25px rgba(0,229,255,0.08); margin-bottom: 25px;">
          
          <!-- Top Grocery Header Bar -->
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(0,229,255,0.25); padding-bottom: 12px; margin-bottom: 16px; flex-wrap: wrap; gap: 10px;">
            <div>
              <span style="background: #00e5ff; color: #030a12; font-weight: 900; font-size: 0.72rem; padding: 2px 8px; border-radius: 3px;">LEVEL 02 ARENA</span>
              <span style="color: #ffffff; font-weight: 800; font-size: 1.05rem; margin-left: 10px; letter-spacing: 1px;">LOCAL BRAND GROCERY STORE &amp; WEEKLY CIRCULAR DEALS</span>
            </div>
            
            <!-- Store Selector -->
            <div style="display: flex; align-items: center; gap: 8px;">
              <span style="font-size: 0.7rem; color: #8ce4a7; font-weight: 700;">CHOOSE STORE:</span>
              <select id="grocery-brand-select" style="background: #01060d; color: #00e5ff; border: 1px solid rgba(0,229,255,0.4); font-size: 0.72rem; padding: 4px 10px; border-radius: 4px; font-weight: 700; cursor: pointer;">
                <option value="kroger" selected>🛒 KROGER // Mega-Savings &amp; Digital Coupons</option>
                <option value="trader_joes">🌻 TRADER JOE'S // Quality Organic &amp; Everyday Value</option>
                <option value="aldi">🪙 ALDI // Frugal Mastery &amp; Deep Discount Staples</option>
                <option value="whole_foods">🌿 WHOLE FOODS // 532nm Clean Organic Nutrition</option>
                <option value="meijer">🍎 MEIJER // Bulk Family Value &amp; Local Produce</option>
              </select>
            </div>
          </div>

          <!-- Grocery Store Aisle Banner -->
          <div style="background: linear-gradient(135deg, rgba(0,229,255,0.1) 0%, rgba(0,255,102,0.08) 100%); border: 1px solid rgba(0,229,255,0.3); border-radius: 6px; padding: 12px 16px; margin-bottom: 18px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
            <div>
              <div style="color: #00e5ff; font-weight: 900; font-size: 0.85rem; letter-spacing: 1px;" id="grocery-store-headline">
                KROGER SUPERMARKET // THIS WEEK'S OFFICIAL DIGITAL CIRCULAR
              </div>
              <div style="color: #b8e2c8; font-size: 0.74rem; line-height: 1.4; margin-top: 3px;">
                Clip weekly digital deals and digital coupons below to build your family&rsquo;s shopping cart. Watch your checkout total drop while boosting your body&rsquo;s <strong>532nm Chlorophyll &amp; Nutrient Vitality</strong>!
              </div>
            </div>
            
            <div style="display: flex; gap: 10px; align-items: center;">
              <div style="background: rgba(0,0,0,0.5); padding: 6px 12px; border-radius: 4px; border: 1px solid rgba(0,255,102,0.3); text-align: center;">
                <div style="font-size: 0.65rem; color: #8ce4a7;">CART SAVINGS:</div>
                <div id="cart-savings-display" style="color: #00ff66; font-weight: 900; font-size: 1.1rem; font-family: 'Share Tech Mono', monospace;">-$0.00</div>
              </div>
              <div style="background: rgba(0,0,0,0.5); padding: 6px 12px; border-radius: 4px; border: 1px solid rgba(0,229,255,0.3); text-align: center;">
                <div style="font-size: 0.65rem; color: #8ce4a7;">CHECKOUT TOTAL:</div>
                <div id="cart-total-display" style="color: #00e5ff; font-weight: 900; font-size: 1.1rem; font-family: 'Share Tech Mono', monospace;">$0.00</div>
              </div>
            </div>
          </div>

          <!-- Weekly Deals & Clippable Coupons Catalog Grid -->
          <div style="margin-bottom: 18px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
              <span style="font-size: 0.74rem; color: #8ce4a7; font-weight: 700; letter-spacing: 1px;">
                📰 OFFICIAL WEEKLY CIRCULAR DEALS (CLICK TO CLIP COUPON &amp; ADD TO CART):
              </span>
              <span style="font-size: 0.7rem; color: #00ff66; font-family: 'Share Tech Mono', monospace;">
                DIGITAL COUPONS AUTO-APPLY
              </span>
            </div>

            <!-- Product Deals Grid -->
            <div class="weekly-deals-catalog" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 12px;">
              
              <!-- Deal 1: Avocados -->
              <div class="deal-card" style="background: rgba(5,15,25,0.75); border: 1px solid rgba(0,255,102,0.25); border-radius: 6px; padding: 12px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="background: rgba(0,255,102,0.15); color: #00ff66; font-size: 0.65rem; font-weight: 800; padding: 2px 6px; border-radius: 3px;">SAVE $2.50</span>
                    <span style="color: #8ce4a7; font-size: 0.68rem; text-decoration: line-through;">$4.99 Reg</span>
                  </div>
                  <div style="color: #ffffff; font-weight: 800; font-size: 0.85rem; margin-bottom: 2px;">🥑 Organic Hass Avocados (4-ct Bag)</div>
                  <div style="font-size: 0.7rem; color: #a0f0c0; line-height: 1.3; margin-bottom: 8px;">
                    Heart-healthy monounsaturated fats &bull; 532nm chlorophyll rich &bull; <strong>Sale: $2.49</strong>
                  </div>
                </div>
                <button type="button" class="btn-clip-deal" data-id="avocado" data-name="Organic Hass Avocados 4-pack" data-sale="2.49" data-reg="4.99" data-vit="6" style="background: rgba(0,255,102,0.15); border: 1px solid #00ff66; color: #ffffff; font-size: 0.72rem; font-weight: 800; padding: 6px 10px; border-radius: 4px; cursor: pointer; transition: all 0.2s ease;">
                  ✂️ CLIP COUPON &amp; ADD (+$2.49)
                </button>
              </div>

              <!-- Deal 2: Wild Salmon -->
              <div class="deal-card" style="background: rgba(5,15,25,0.75); border: 1px solid rgba(0,229,255,0.25); border-radius: 6px; padding: 12px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="background: rgba(0,229,255,0.15); color: #00e5ff; font-size: 0.65rem; font-weight: 800; padding: 2px 6px; border-radius: 3px;">SAVE $4.00/lb</span>
                    <span style="color: #8ce4a7; font-size: 0.68rem; text-decoration: line-through;">$11.99/lb Reg</span>
                  </div>
                  <div style="color: #ffffff; font-weight: 800; font-size: 0.85rem; margin-bottom: 2px;">🐟 Wild Atlantic Salmon Fillets (1 lb)</div>
                  <div style="font-size: 0.7rem; color: #a0f0c0; line-height: 1.3; margin-bottom: 8px;">
                    High Omega-3 DHA/EPA for brain focus &amp; heart &bull; <strong>Sale: $7.99/lb</strong>
                  </div>
                </div>
                <button type="button" class="btn-clip-deal" data-id="salmon" data-name="Wild Atlantic Salmon Fillet" data-sale="7.99" data-reg="11.99" data-vit="10" style="background: rgba(0,229,255,0.15); border: 1px solid #00e5ff; color: #ffffff; font-size: 0.72rem; font-weight: 800; padding: 6px 10px; border-radius: 4px; cursor: pointer; transition: all 0.2s ease;">
                  ✂️ CLIP DEAL &amp; ADD (+$7.99)
                </button>
              </div>

              <!-- Deal 3: Organic Milk / Oatmilk -->
              <div class="deal-card" style="background: rgba(5,15,25,0.75); border: 1px solid rgba(255,170,0,0.25); border-radius: 6px; padding: 12px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="background: rgba(255,170,0,0.15); color: #ffaa00; font-size: 0.65rem; font-weight: 800; padding: 2px 6px; border-radius: 3px;">BOGO 50% OFF</span>
                    <span style="color: #8ce4a7; font-size: 0.68rem; text-decoration: line-through;">$5.99 Reg</span>
                  </div>
                  <div style="color: #ffffff; font-weight: 800; font-size: 0.85rem; margin-bottom: 2px;">🥛 Pasture-Raised Milk or Oatmilk (Gallon)</div>
                  <div style="font-size: 0.7rem; color: #a0f0c0; line-height: 1.3; margin-bottom: 8px;">
                    Calcium &amp; Vitamin D3 fortification for family &bull; <strong>Sale: $3.49</strong>
                  </div>
                </div>
                <button type="button" class="btn-clip-deal" data-id="milk" data-name="Pasture Milk/Oatmilk Gal" data-sale="3.49" data-reg="5.99" data-vit="5" style="background: rgba(255,170,0,0.15); border: 1px solid #ffaa00; color: #ffffff; font-size: 0.72rem; font-weight: 800; padding: 6px 10px; border-radius: 4px; cursor: pointer; transition: all 0.2s ease;">
                  ✂️ CLIP BOGO &amp; ADD (+$3.49)
                </button>
              </div>

              <!-- Deal 4: Broccoli & Organic Greens -->
              <div class="deal-card" style="background: rgba(5,15,25,0.75); border: 1px solid rgba(0,255,102,0.25); border-radius: 6px; padding: 12px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="background: rgba(0,255,102,0.15); color: #00ff66; font-size: 0.65rem; font-weight: 800; padding: 2px 6px; border-radius: 3px;">2 FOR $3.00</span>
                    <span style="color: #8ce4a7; font-size: 0.68rem; text-decoration: line-through;">$4.50 Reg</span>
                  </div>
                  <div style="color: #ffffff; font-weight: 800; font-size: 0.85rem; margin-bottom: 2px;">🥦 Fresh Broccoli Crowns &amp; Baby Spinach</div>
                  <div style="font-size: 0.7rem; color: #a0f0c0; line-height: 1.3; margin-bottom: 8px;">
                    532nm phytonutrients, folate &amp; clean detox &bull; <strong>Sale: $1.50 ea</strong>
                  </div>
                </div>
                <button type="button" class="btn-clip-deal" data-id="greens" data-name="Broccoli Crowns & Baby Spinach" data-sale="1.50" data-reg="2.75" data-vit="8" style="background: rgba(0,255,102,0.15); border: 1px solid #00ff66; color: #ffffff; font-size: 0.72rem; font-weight: 800; padding: 6px 10px; border-radius: 4px; cursor: pointer; transition: all 0.2s ease;">
                  ✂️ CLIP DEAL &amp; ADD (+$1.50)
                </button>
              </div>

              <!-- Deal 5: Bulk Jasmine Rice & Quinoa -->
              <div class="deal-card" style="background: rgba(5,15,25,0.75); border: 1px solid rgba(213,0,249,0.25); border-radius: 6px; padding: 12px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="background: rgba(213,0,249,0.15); color: #d500f9; font-size: 0.65rem; font-weight: 800; padding: 2px 6px; border-radius: 3px;">SAVE $3.50</span>
                    <span style="color: #8ce4a7; font-size: 0.68rem; text-decoration: line-through;">$9.49 Reg</span>
                  </div>
                  <div style="color: #ffffff; font-weight: 800; font-size: 0.85rem; margin-bottom: 2px;">🌾 Bulk Brown Jasmine Rice (5 lb Bag)</div>
                  <div style="font-size: 0.7rem; color: #a0f0c0; line-height: 1.3; margin-bottom: 8px;">
                    Low glycemic family staple &bull; 30-day carbohydrate foundation &bull; <strong>Sale: $5.99</strong>
                  </div>
                </div>
                <button type="button" class="btn-clip-deal" data-id="rice" data-name="Brown Jasmine Rice 5lb" data-sale="5.99" data-reg="9.49" data-vit="6" style="background: rgba(213,0,249,0.15); border: 1px solid #d500f9; color: #ffffff; font-size: 0.72rem; font-weight: 800; padding: 6px 10px; border-radius: 4px; cursor: pointer; transition: all 0.2s ease;">
                  ✂️ CLIP DEAL &amp; ADD (+$5.99)
                </button>
              </div>

              <!-- Deal 6: Diapers & Baby Care (Working Mother Relief) -->
              <div class="deal-card" style="background: rgba(5,15,25,0.75); border: 1px solid rgba(255,170,0,0.25); border-radius: 6px; padding: 12px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="background: rgba(255,170,0,0.15); color: #ffaa00; font-size: 0.65rem; font-weight: 800; padding: 2px 6px; border-radius: 3px;">SAVE $6.00</span>
                    <span style="color: #8ce4a7; font-size: 0.68rem; text-decoration: line-through;">$22.99 Reg</span>
                  </div>
                  <div style="color: #ffffff; font-weight: 800; font-size: 0.85rem; margin-bottom: 2px;">👶 Baby Diapers &amp; Sensitive Wipes Value Pack</div>
                  <div style="font-size: 0.7rem; color: #a0f0c0; line-height: 1.3; margin-bottom: 8px;">
                    Essential household family item for working mothers &bull; <strong>Sale: $16.99</strong>
                  </div>
                </div>
                <button type="button" class="btn-clip-deal" data-id="diapers" data-name="Baby Diapers Value Pack" data-sale="16.99" data-reg="22.99" data-vit="4" style="background: rgba(255,170,0,0.15); border: 1px solid #ffaa00; color: #ffffff; font-size: 0.72rem; font-weight: 800; padding: 6px 10px; border-radius: 4px; cursor: pointer; transition: all 0.2s ease;">
                  ✂️ CLIP COUPON &amp; ADD (+$16.99)
                </button>
              </div>

            </div>
          </div>

          <!-- Checkout Register & Cart Summary Station -->
          <div style="background: rgba(4,10,18,0.95); border: 1px solid rgba(0,229,255,0.3); border-radius: 6px; padding: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
              <div>
                <span style="color: #ffffff; font-weight: 800; font-size: 0.9rem;">🛒 YOUR GROCERY CART:</span>
                <span id="cart-item-count" style="color: #00e5ff; font-weight: 700; font-size: 0.8rem; margin-left: 6px;">0 Items</span>
              </div>
              <div style="font-family: 'Share Tech Mono', monospace; font-size: 0.72rem; color: #8ce4a7;">
                NUTRITIONAL CLARITY: <span id="cart-vitality-score" style="color: #00ff66; font-weight: 800;">100% [532nm OPTIMAL]</span>
              </div>
            </div>

            <!-- Active Cart Items List -->
            <div id="cart-items-list" style="font-size: 0.72rem; color: #b8e2c8; background: #010408; border: 1px solid rgba(255,255,255,0.1); border-radius: 4px; padding: 8px 12px; min-height: 48px; max-height: 120px; overflow-y: auto; margin-bottom: 12px;">
              <span style="color: #64748b;">Cart is empty. Click any weekly deal button above to clip digital coupons and build your cart!</span>
            </div>

            <!-- Checkout Action Bar -->
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
              <div>
                <button type="button" id="btn-clear-grocery-cart" style="background: rgba(255,60,60,0.12); border: 1px solid rgba(255,60,60,0.3); color: #ff6666; font-size: 0.7rem; font-weight: 700; padding: 6px 12px; border-radius: 4px; cursor: pointer;">
                  ↺ EMPTY CART
                </button>
              </div>

              <div style="display: flex; gap: 10px; align-items: center;">
                <button type="button" id="btn-checkout-grocery" style="background: #00ff66; color: #02070f; border: none; font-size: 0.8rem; font-weight: 900; padding: 10px 18px; border-radius: 4px; cursor: pointer; box-shadow: 0 0 14px rgba(0,255,102,0.4); transition: all 0.2s ease;">
                  💳 SCAN &amp; PAY FROM BANK CHECKING WITH DIGITAL COUPONS
                </button>
              </div>
            </div>

            <!-- Receipt & Impact Feed -->
            <div id="grocery-receipt-feed" style="margin-top: 10px; font-family: 'Share Tech Mono', monospace; font-size: 0.7rem; color: #8ce4a7; line-height: 1.4;">
              ⟦ CASHIER SCANNER ⟧ Ready for checkout. Digital coupons will be automatically subtracted from your total.
            </div>

          </div>

        </div>


        <!-- ===================================================================
             LEVEL 03 DISPLAY CONTAINER: PHARMACY, HEALTH & UTILITIES
             =================================================================== -->
        <div class="level-content-pane" id="level-pane-3" style="display: none; background: rgba(3,12,22,0.9); border: 1px solid rgba(213,0,249,0.35); border-radius: 8px; padding: 20px; box-shadow: 0 0 25px rgba(213,0,249,0.08); margin-bottom: 25px;">
          
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(213,0,249,0.25); padding-bottom: 12px; margin-bottom: 16px;">
            <div>
              <span style="background: #d500f9; color: #ffffff; font-weight: 900; font-size: 0.72rem; padding: 2px 8px; border-radius: 3px;">LEVEL 03 ARENA</span>
              <span style="color: #ffffff; font-weight: 800; font-size: 1.05rem; margin-left: 10px; letter-spacing: 1px;">PHARMACY, WELLNESS &amp; HOUSEHOLD UTILITIES</span>
            </div>
            <div style="font-size: 0.7rem; color: #d500f9; font-family: 'Share Tech Mono', monospace;">
              RX &amp; BILL OPTIMIZER: <span style="color: #00ff66; font-weight: 800;">ACTIVE</span>
            </div>
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; margin-bottom: 16px;">
            
            <!-- Pharmacy Prescription Pick-Up -->
            <div style="background: rgba(6,16,28,0.8); border: 1px solid rgba(0,255,102,0.3); border-radius: 6px; padding: 14px;">
              <div style="color: #00ff66; font-weight: 800; font-size: 0.85rem; margin-bottom: 4px;">💊 CVS / LOCAL COMMUNITY PHARMACY</div>
              <div style="font-size: 0.75rem; color: #b8e2c8; line-height: 1.4; margin-bottom: 10px;">
                Fulfill sight prescription and cellular phototherapy vitamins (Vitamin D3/K2, EPA/DHA Omega-3).
              </div>
              <button type="button" id="btn-fulfill-rx" style="background: rgba(0,255,102,0.15); border: 1px solid #00ff66; color: #ffffff; font-size: 0.72rem; font-weight: 800; padding: 6px 12px; border-radius: 4px; cursor: pointer;">
                ✓ REFILL SIGHT PRESCRIPTION (-$25.00 // +12% VITALITY)
              </button>
            </div>

            <!-- Home Utilities Negotiation -->
            <div style="background: rgba(6,16,28,0.8); border: 1px solid rgba(213,0,249,0.3); border-radius: 6px; padding: 14px;">
              <div style="color: #d500f9; font-weight: 800; font-size: 0.85rem; margin-bottom: 4px;">⚡ POWER &amp; GIGABIT FIBER UTILITIES</div>
              <div style="font-size: 0.75rem; color: #b8e2c8; line-height: 1.4; margin-bottom: 10px;">
                Monthly electric, clean water, and internet bills total $285/mo. Deploy AI utility negotiator to lower rates.
              </div>
              <button type="button" id="btn-negotiate-utilities" style="background: rgba(213,0,249,0.15); border: 1px solid #d500f9; color: #ffffff; font-size: 0.72rem; font-weight: 800; padding: 6px 12px; border-radius: 4px; cursor: pointer;">
                🤖 DEPLOY AI BILL NEGOTIATOR (SAVE $45/MO PERMANENTLY)
              </button>
            </div>

          </div>

          <div id="level-3-feed" style="font-family: 'Share Tech Mono', monospace; font-size: 0.7rem; color: #8ce4a7; background: #010408; padding: 8px 12px; border-radius: 4px; border: 1px solid rgba(213,0,249,0.2);">
            ⟦ PHARMACY HUD ⟧ Prescription status aligned with Step 02 vision dial. Utilities operating at standard baseline.
          </div>

        </div>


        <!-- ===================================================================
             LEVEL 04 DISPLAY CONTAINER: MASTER REAL-WORLD HARMONY & FREEDOM STATUS
             =================================================================== -->
        <div class="level-content-pane" id="level-pane-4" style="display: none; background: rgba(3,12,22,0.9); border: 1px solid rgba(255,170,0,0.35); border-radius: 8px; padding: 20px; box-shadow: 0 0 25px rgba(255,170,0,0.08); margin-bottom: 25px;">
          
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,170,0,0.25); padding-bottom: 12px; margin-bottom: 16px;">
            <div>
              <span style="background: #ffaa00; color: #02070f; font-weight: 900; font-size: 0.72rem; padding: 2px 8px; border-radius: 3px;">LEVEL 04 ARENA</span>
              <span style="color: #ffffff; font-weight: 800; font-size: 1.05rem; margin-left: 10px; letter-spacing: 1px;">MASTER REAL-WORLD HARMONY &amp; FREEDOM STATUS</span>
            </div>
            <div style="font-size: 0.7rem; color: #00ff66; font-family: 'Share Tech Mono', monospace;">
              532nm GREEN EQUILIBRIUM: <span style="font-weight: 800;">ACHIEVED</span>
            </div>
          </div>

          <div style="background: rgba(0,0,0,0.45); border: 1px solid rgba(0,255,102,0.3); border-radius: 6px; padding: 16px; margin-bottom: 16px; text-align: center;">
            <div style="font-size: 0.75rem; color: #8ce4a7; margin-bottom: 4px;">CONSOLIDATED REAL-WORLD SCORE:</div>
            <div id="master-real-world-score" style="font-size: 2.2rem; font-weight: 900; color: #00ff66; font-family: 'Share Tech Mono', monospace; line-height: 1;">
              94.6% // SOVEREIGN LIFE FREEDOM
            </div>
            <div style="font-size: 0.8rem; color: #ffffff; margin-top: 6px; font-weight: 700;">
              ✨ Bank Liquidity Managed &bull; Grocery Weekly Deals Clipped &bull; 532nm Cellular Vitality Protected
            </div>
            <p style="color: #b8e2c8; font-size: 0.75rem; max-width: 680px; margin: 8px auto 0 auto; line-height: 1.4;">
              By balancing smart liquidity at the bank and mastering the weekly deals at your local brand grocery store, you have eliminated daily financial panic and nourished your body&rsquo;s nervous system.
            </p>
          </div>

          <div style="display: flex; justify-content: center; gap: 10px;">
            <a href="#spectrum-monopoly" class="cyber-btn sm" style="border-color: #00ff66; color: #00ff66; text-decoration: none; font-weight: 800; padding: 8px 16px;">
              <span>APPLY HARMONY TROPHY TO SPECTRUM MONOPOLY</span> <span>↓</span>
            </a>
          </div>

        </div>

      </div>
'''

# Check if already present
if 'id="real-world-levels-experience"' in home:
    print("WARNING: real-world-levels-experience already present in homepage.html! Skipping duplicate injection.")
else:
    # Target location: right before `<!-- =========================================================================\n           PART 3: BONUS SHADERTOY WORLD-SHADING & ENLIGHTENMENT SANDBOX`
    pattern = r'(\s*<!-- =+\s*PART 3: BONUS SHADERTOY WORLD-SHADING)'
    match = re.search(pattern, home)
    if not match:
        pattern = r'(<div class="shadertoy-bonus-sandbox-wrapper" id="shadertoy-bonus-studio")'
        match = re.search(pattern, home)
    
    if match:
        print("Found injection point before Bonus Shadertoy Studio.")
        home = home[:match.start()] + '\n' + REAL_WORLD_LEVELS_HTML + '\n\n' + home[match.start():]
    else:
        print("ERROR: Could not find injection point before Shadertoy bonus studio!")
        exit(1)

with open(HOMEPAGE_PATH, 'w', encoding='utf-8') as f:
    f.write(home)

print(f"Injected Real-World Levels HTML. New size: {len(home)} characters.")
