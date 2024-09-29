import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPaperPlane, faPhone } from '@fortawesome/free-solid-svg-icons';
import './AskAI.css';

const AskAI = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');

    // Initial greeting message
    useEffect(() => {
        setMessages([
            {
                sender: 'bot',
                text: "You can call me at 180011234, if you don't like texting :P"
            }
        ]);
    }, []);

    const handleInputChange = (e) => {
        setInput(e.target.value);
    };

    const handleSendMessage = async () => {
        if (input.trim()) {
            const newMessages = [...messages, { sender: 'user', text: input }];
            setMessages(newMessages);
            setInput('');

            try {
                const response = await axios.post('https://your-gemini-api-endpoint.com', {
                    message: input,
                });
                setMessages([...newMessages, { sender: 'bot', text: response.data.reply }]);
            } catch (error) {
                console.error('Error communicating with the AI service:', error);
            }
        }
    };

    return (
        <div className="chat-container">
            <div className="chat-window">
                <div className="messages">
                    {messages.map((msg, index) => (
                        <div key={index} className={msg.sender}>
                            {msg.text}
                        </div>
                    ))}
                </div>
                <div className="input-area">
                    <input
                        type="text"
                        value={input}
                        onChange={handleInputChange}
                        placeholder="Type a message..."
                    />
                    <button onClick={handleSendMessage} title="Send">
                        <FontAwesomeIcon icon={faPaperPlane} />
                    </button>
                </div>
            </div>
            <div className="call-options">
                <button onClick={() => alert('Call option not implemented yet.')} title="Call">
                    <FontAwesomeIcon icon={faPhone} />
                </button>
            </div>
        </div>
    );
};

export default AskAI;
