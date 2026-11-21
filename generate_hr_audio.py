import asyncio
import edge_tts
import os
import json
import shutil
import subprocess

def get_ffmpeg_exe():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        exe = shutil.which('ffmpeg')
        if exe:
            return exe
        raise RuntimeError("FFmpeg executable not found. Install ffmpeg or 'pip install imageio-ffmpeg'.")

scripts = {
    1: "Welcome to Falkor. We are delighted to have you join our team. This orientation provides an essential guide to our history, our leadership, how we work, and the HR policies that support and protect you from your very first day.",
    2: "Established in Abu Dhabi in 1979, Falkor has grown from a specialized trading house into a premier partner for the Oil, Gas, Power, and Utilities sectors. Today, with over fifteen hundred professionals and ISO certification, our four core divisions deliver turnkey engineering, procurement, maintenance, and manpower across the Emirates.",
    3: "We operate at the highest institutional tiers, serving national energy leaders including ADNOC Group, ADDC, and Abu Dhabi Airports. Our performance scores are audited continuously. Remember: any safety breach by an individual is recorded against Falkor as a company. Where client standards are stricter than ours, client rules strictly apply.",
    4: "Falkor is led by Chairman Mister Sam Mebarek, Chief Executive Officer Mister Mehdi Mebarek, Chief Operating Officer Mister Muralidharan Swaminathan, Director of Finance, Admin, HR and IT, Mister Jignesh Patel, and Sales Director Mister Jamal. Our headquarters is located at Level 52, Addax Tower, Al Reem Island, phone zero two, six three four, two five five five, supported by our central workshop facility in Mussafah Industrial Area.",
    5: "Our appearance inspires professional trust. Monday through Thursday requires formal business attire, with smart casual permitted on Fridays. All client interactions require full formal attire regardless of the day. When visiting workshops or active project sites, company-issued coveralls and approved safety footwear are mandatory at all times.",
    6: "Standard office hours are from 8:00 AM to 5:00 PM with a one-hour lunch break, totaling forty hours per week. During the holy month of Ramadan, hours are reduced to six hours per day. All timesheets must be submitted through the HR Portal by Sunday 10:00 AM. Any overtime must be pre-approved in writing.",
    7: "A well-run workplace reflects our operational excellence. Practice a clean-desk policy each evening and shred sensitive documents. Smoking is strictly prohibited inside the office and only permitted in designated external zones. All visitors must be logged and escorted, and conference rooms booked in advance.",
    8: "Health, Safety, and Environment is our highest operational priority. Familiarize yourself immediately with your floor evacuation warden and assembly points. Approved Personal Protective Equipment must be worn in designated operational areas, and we maintain an absolute zero-tolerance policy regarding alcohol and prohibited substances.",
    9: "In an emergency, dial nine nine seven for Fire, nine nine eight for Ambulance, and nine nine nine for Police, then notify your HSE Officer immediately. Report all hazards and near-misses within twenty-four hours. Every Falkor employee holds Stop Work Authority: if you see any unsafe condition, stop the work immediately without fear of penalty.",
    10: "When deployed to ADNOC or government client sites, you must complete the client's mandatory site induction before beginning work. Gate passes and vehicle permits must be valid. Strictly obey all posted speed limits and Life-Saving Rules. Mobile phone usage is strictly prohibited across active operational plant zones.",
    11: "Integrity is fundamental to our reputation. All client specifications, drawings, pricing models, and financial data are strictly confidential. Your Non-Disclosure Agreement applies both during your employment and after departure. Disclosing proprietary data to outside parties constitutes gross misconduct.",
    12: "Probation begins on your first day for all new hires. The standard probation period is one to three months as stated in your contract, extendable up to a maximum of six months with formal approval. Fourteen days written notice is required during probation. You will agree SMART performance objectives with your Line Manager in your first weeks.",
    13: "Falkor provides comprehensive leave under UAE Labour Law. Employees receive thirty calendar days of paid annual leave per year. Sick leave is available up to ninety days per year subject to medical certificates. We also provide paid maternity leave of sixty days, five days of parental leave, bereavement leave, and study leave.",
    14: "Plan and submit your annual leave requests at least thirty days in advance. You must report back to duty on the first working day following your approved leave. For sick leave, an official medical certificate licensed by health authorities must be submitted to HR within forty-eight hours of absence.",
    15: "Salaries are disbursed monthly through the UAE Wages Protection System on the last working day of each month. Your compensation consists of basic salary and allowances. Falkor provides comprehensive medical and life insurance coverage. Employees who complete probation become eligible for company personal loan facilities.",
    16: "Falkor is committed to employee welfare. All wages are protected by law, and eligible employees receive an annual flight allowance. End of Service Gratuity accrues from day one and becomes payable upon completing one year of continuous service. We ensure dignified workplace conditions and zero tolerance for discrimination.",
    17: "Our performance cycle is built on transparent development. In January, you agree SMART objectives with your Line Manager. A mid-year review in June ensures progress is on track, followed by your annual evaluation in December. Your appraisal results directly guide promotions, salary increments, and professional development.",
    18: "Our disciplinary procedure ensures fairness and accountability. When an offence occurs, you receive written notice within five working days, followed by a formal investigation. You will always present your case to the Disciplinary Committee before any decision. Violations progress from formal warnings to dismissal, while gross misconduct allows immediate termination.",
    19: "When concluding your tenure with Falkor, resignations must be submitted in writing with contract notice observed. End of Service Gratuity is calculated at twenty-one days of basic pay per year for the first five years, and thirty days thereafter. HR ensures all full and final settlements and visa cancellations are executed transparently.",
    20: "We protect your voice. If you experience an issue, speak with your Line Manager or HR. Formal grievances are investigated confidentially and resolved within seven working days, strictly protected against retaliation. For contracts, benefits, and support, contact HR at h r at falkor dash eng dot com or call zero two, six three four, two five five five.",
    21: "At Falkor, we are more than colleagues; we are an extended family committed to excellence, mutual support, and celebrating success together. You can access the complete Employee Policies Handbook anytime on our careers portal. Once again, welcome aboard, and we wish you an extraordinary career with Falkor."
}

async def generate_all():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    audio_dir = os.path.join(base_dir, "audio")
    os.makedirs(audio_dir, exist_ok=True)
    voice = "en-US-JennyNeural"
    
    durations = {}
    ffmpeg = get_ffmpeg_exe()
    
    for num, text in scripts.items():
        out_file = os.path.join(audio_dir, f"slide_{num:02d}.mp3")
        comm = edge_tts.Communicate(text, voice, rate="-3%")
        await comm.save(out_file)
        
        # Get duration via ffmpeg
        p = subprocess.run([ffmpeg, '-i', out_file], stderr=subprocess.PIPE, text=True)
        dur = 0.0
        for line in p.stderr.split('\n'):
            if 'Duration:' in line:
                # Duration: 00:00:25.78,
                tstr = line.split('Duration:')[1].split(',')[0].strip()
                h, m, s = tstr.split(':')
                dur = float(h)*3600 + float(m)*60 + float(s)
                break
        durations[num] = round(dur, 2)
        print(f"Slide {num:02d} audio generated: {durations[num]}s -> {out_file}")
        
    durations_file = os.path.join(base_dir, "audio_durations.json")
    with open(durations_file, "w") as f:
        json.dump(durations, f, indent=2)
    print(f"All 21 audio files generated successfully! Total duration: {sum(durations.values())/60:.2f} minutes")

if __name__ == "__main__":
    asyncio.run(generate_all())

