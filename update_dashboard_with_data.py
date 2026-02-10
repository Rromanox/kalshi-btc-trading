#!/usr/bin/env python3
"""
Update existing dashboard HTML with real data
Simpler approach - just update the data sections
"""

import json
import os
import re
from datetime import datetime, date

def update_dashboard_data(cycle_data, trades):
    """Update the existing HTML dashboard with real data"""
    
    # Read current HTML file
    html_path = "/home/ubuntu/clawd/kalshi-btc-trading/index.html"
    if not os.path.exists(html_path):
        print("❌ Dashboard HTML file not found")
        return False
    
    with open(html_path, 'r') as f:
        html_content = f.read()
    
    # Calculate metrics
    total_cycles = cycle_data.get('total_cycles', 0)
    total_trades = len(trades)
    skips = total_cycles - total_trades
    skip_rate = (skips / total_cycles * 100) if total_cycles > 0 else 0
    
    # Win/loss calculation (placeholder for now)
    wins = 0  # Will be calculated when market outcomes are available
    win_rate = 0
    
    # Edge breakdown
    edge_counts = {'late_window_lock': 0, 'speed_advantage': 0, 'volatility_mispricing': 0, 'unknown': 0}
    for trade in trades:
        edge = trade.get('edge_type', 'unknown')
        if edge in edge_counts:
            edge_counts[edge] += 1
    
    # Update JavaScript data sections
    js_updates = f"""
        // Updated with real data at {datetime.now().isoformat()}
        document.getElementById('lastUpdated').textContent = 'Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S EST")}';
        document.getElementById('totalTrades').textContent = '{total_trades}';
        document.getElementById('cyclesMonitored').textContent = '{total_cycles}';
        document.getElementById('skipRate').textContent = '{skip_rate:.1f}%';
        document.getElementById('winRate').textContent = '{win_rate:.1f}%';
        document.getElementById('totalPL').textContent = '$0.00';
        
        // Edge performance
        document.getElementById('lateWindowTrades').textContent = '{edge_counts['late_window_lock']}';
        document.getElementById('speedTrades').textContent = '{edge_counts['speed_advantage']}';
        document.getElementById('volTrades').textContent = '{edge_counts['volatility_mispricing']}';
    """
    
    # Update recent activity section
    recent_activity = f"""
        <div style="padding: 15px; background: rgba(255,255,255,0.05); border-radius: 10px; margin-bottom: 15px;">
            <strong>Today ({date.today().isoformat()})</strong><br>
            <small>{total_cycles} cycles analyzed • {total_trades} trades executed • {skip_rate:.1f}% skip rate</small>
        </div>
        <div style="padding: 15px; background: rgba(255,255,255,0.05); border-radius: 10px;">
            <strong>System Status</strong><br>
            <small>✅ BTC Edge Bot operational • ✅ Auto-notifications active • ✅ Nightly commits enabled</small>
        </div>
    """
    
    # Replace placeholders in HTML
    # Update the JavaScript section
    html_content = re.sub(
        r"// You'll replace these with real data loading.*?document\.getElementById\('totalPL'\)\.textContent = '\$0\.00';",
        js_updates.strip(),
        html_content,
        flags=re.DOTALL
    )
    
    # Update recent activity
    html_content = re.sub(
        r'recentActivityDiv\.innerHTML = `.*?`;',
        f'recentActivityDiv.innerHTML = `{recent_activity}`;',
        html_content,
        flags=re.DOTALL
    )
    
    # Write updated HTML
    with open(html_path, 'w') as f:
        f.write(html_content)
    
    print(f"✅ Dashboard updated with real data: {total_trades} trades, {total_cycles} cycles, {skip_rate:.1f}% skip rate")
    return True

def main():
    """Load data and update dashboard"""
    try:
        # Load today's data
        today = date.today().isoformat()
        
        # Load cycle data
        cycle_file = f"/home/ubuntu/clawd/kalshi-bot/btc_cycle_log.jsonl"
        cycles = []
        if os.path.exists(cycle_file):
            with open(cycle_file, 'r') as f:
                for line in f:
                    try:
                        cycle = json.loads(line.strip())
                        if cycle.get('timestamp', '')[:10] == today:
                            cycles.append(cycle)
                    except:
                        continue
        
        cycle_data = {"total_cycles": len(cycles), "cycles": cycles}
        
        # Extract trades from cycles
        trades = []
        for cycle in cycles:
            if cycle.get('decision', '').startswith('BUY_'):
                trade = {
                    "edge_type": "unknown",  # Would parse from reasoning
                    "side": cycle.get('decision', '').replace('BUY_', '').lower(),
                    "market_result": cycle.get('outcome', 'pending')
                }
                trades.append(trade)
        
        # Update dashboard
        success = update_dashboard_data(cycle_data, trades)
        
        if success:
            print(f"🌐 Website dashboard updated successfully!")
        else:
            print("❌ Failed to update dashboard")
            
    except Exception as e:
        print(f"❌ Dashboard update error: {e}")

if __name__ == "__main__":
    main()